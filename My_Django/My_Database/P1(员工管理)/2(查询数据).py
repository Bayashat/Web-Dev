import pymysql


#   1. 连接MySQL 
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root123", charset='utf8', db='unicom') # 表示当前电脑上的主机

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 进行收发数据, 指令

#   2. 发送指令(千万不要用字符串格式化去做SQL的拼接, 安全隐患SQL注入)

# sql = "select * from admin where id > %s"         # 这样也可以
# cursor.execute(sql, [2, ]) 

sql = "select * from admin where id > 2" 
cursor.execute(sql) 

# 获取符合条件的所有数据, 得到的是 "列表里套字典"  没数据就是: 空列表
data_list = cursor.fetchall()  # 获取数据库发来的值    如果写 curson.fetchone()  那只会返回满足条件的第一条数据
for row_dict in data_list:
    print(row_dict) 

#   3. 关闭连接
cursor.close()
conn.close()