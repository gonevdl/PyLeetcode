"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
"""

import pymysql
import py0001

# 创建链接
connection = pymysql.connect(host="127.0.0.1", user="root", port=3306, password="L&hx520.", database="lhxtestdb",
                             charset="utf8mb4")

for sequence in py0001.result:
    try:
        with connection.cursor() as cursor:
            affected_rows = cursor.execute('insert into `discount` value (%s)', sequence)
            if affected_rows == 1:
                print("添加成功！")
        connection.commit()
    except pymysql.MySQLError as err:
        connection.rollback()
        print(type(err), err)
