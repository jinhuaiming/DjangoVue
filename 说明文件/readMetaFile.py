import glob
import math
import psycopg2
import time


# 数据库插入函数
def insert_data(cur, data):
    cur.execute(f'insert into argo.argofloat values (%s,%s,%s,%s,%s,%s)',
                (data['PLATFORMNUMBER'], data['DATACENTRE'], data['LAUNCHDATE'][0:14], data['LAUNCHLATITUDE'],
                 data['LAUNCHLONGITUDE'], data['PROJECTNAME']))


# 文件路径
filename = r'E:\Argo\metafile\*.dat'
# 每个文件读取的数据
# PROJECT NAME
# LAUNCH LONGITUDE
# LAUNCH LATITUDE
# LAUNCH DATE
# DATA CENTRE
dict1 = dict()

# 连接数据库
connection = psycopg2.connect(host='localhost',
                              port=5432,
                              user='postgres',
                              password='jinhu19980613',
                              database='postgres'
                              )
cur = connection.cursor()

time_start = time.time()
# 遍历文件夹里的每个文件
for item in glob.glob(filename):
    # 打开*.dat文件
    with open(item, 'r', encoding='utf-8') as file:
        # 遍历每个打开的*.dat文件的每行数据
        list_data = [item.replace(' ', '').strip().split(':', 1) for item in file.readlines() if
                     item.count(':') == 1 or item.count(':') == 2]

        dict_data = dict(list_data)

        try:
            print(item, '上传成功！')
            insert_data(cur, dict_data)
        except:
            print(dict_data)
        # 关闭每次遍历的文件
        # file.close()
# 关闭数据库连接
connection.commit()
connection.close()

time_end = time.time()

print(f'总运行时间为：{math.floor(time_end - time_start)}秒')
