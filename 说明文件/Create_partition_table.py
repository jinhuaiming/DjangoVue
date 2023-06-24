import psycopg2 as pg


def create_partition_table():
    sql = ''
    # 连接数据库
    conn = pg.connect(database="postgres", user="postgres", password="jinhu19980613", host="127.0.0.1", port="5432")
    # 操作argo元数据的游标
    cur = conn.cursor()
    # 创建批量分区表的游标
    cur1 = conn.cursor()
    # 执行查询所有argo元数据的sql
    cur.execute('select * from argo.argofloat')
    conn.commit()

    # 遍历所有的argo元数据的信息，根据浮标表编号和建分区表sql语句，批量创建分区表
    for index, item in enumerate(cur.fetchall()):
        sql = f'CREATE TABLE argo.argocore{item[0]} PARTITION OF argo.argocore FOR VALUES IN ({item[0]});\n'
        cur1.execute(sql)
        conn.commit()
    conn.close()


if __name__ == '__main__':
    create_partition_table()
