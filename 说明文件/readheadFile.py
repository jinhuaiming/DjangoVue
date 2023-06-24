import os
import glob
import psycopg2


def RemoveValuesoOfList(list_data: list) -> list:
    """
    用于去除数组里的空元素('')
    :param list_data: 数组
    :return: 数组
    """
    list_new_data = []
    for item in list_data:
        if len(item) != 0:
            list_new_data.append(item)
    return list_new_data


def read_one_file(file_path: str) -> list:
    """
    读取一个dat文件，并返回一个二维的数组[[],[],[..]]
    :param file_path: 读取的文件的绝对路径
    :return: 二维的数组
    """
    with open(file_path) as file:
        list_data = file.readlines()
        start = list_data.index('==========================================================================\n')

        list_top_data = [item.strip().split(':', 1)[1] for item in list_data if
                         (item.count(':') == 1 or item.count(':') == 2 | 3) and
                         item.strip().split(':', 1)[0].replace(' ', '') in [
                             'PLATFORMNUMBER', 'CYCLENUMBER', 'JULIANDAY', 'DATE', 'LATITUDE', 'LONGITUDE'
                         ]]
        list_top_data[2] = list_top_data[2].split(' ', 1)[0]
    file.close()
    return list_top_data


def insert_database(cur, sql, data) -> int:
    """
    指定数据读入数据库
    :param cur: 游标对象
    :param sql: SQL语句
    :param data:
    :return:
    """
    cur.execute(sql, data)


if __name__ == '__main__':
    # 遍历每个文件夹

    conn = psycopg2.connect(host='localhost',
                            port=5432,
                            user='postgres',
                            password='jinhu19980613',
                            database='postgres'
                            )
    cur = conn.cursor()

    sql = 'insert into argo.argoheader values (%s,%s,%s,%s,%s,%s)'

    for item_dir_name in os.listdir('E:\Argo\Argocore'):
        # 遍历每个文件夹的文件
        for item_file_name in glob.glob(fr'E:\Argo\Argocore\{item_dir_name}\*.dat'):
            list_sql_data = read_one_file(item_file_name)
            try:
                insert_database(cur, sql, list_sql_data)
                print(f'{item_file_name}上传完成！')
            except:
                try:
                    insert_database(cur, sql, list_sql_data)
                except:
                    print(f'*************{item_file_name}****************')
        conn.commit()

