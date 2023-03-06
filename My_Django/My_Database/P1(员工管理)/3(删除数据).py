import pymysql


#   1. 连接MySQL 
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root123", charset='utf8', db='unicom', autocommit=True) # 表示当前电脑上的主机

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 进行收发数据, 指令

#   2. 发送指令(千万不要用字符串格式化去做SQL的拼接, 安全隐患SQL注入)
sql = "delete from admin where id > %s" 
cursor.execute(sql, [2, ]) 
#   2. 发送指令(千万不要用字符串格式化去做SQL的拼接, 安全隐患SQL注入)
# sql = "delete from admin where id > %s" 
# cursor.execute(sql, [2, ]) 

sql = "delete from admin where id > 2" 
cursor.execute(sql) 


# conn.commit()  # 是用来提交的.  当数据库名字后没有写autocommit时需要写这个


#   3. 关闭连接
cursor.close()
conn.close()