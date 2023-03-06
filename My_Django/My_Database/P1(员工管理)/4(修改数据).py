import pymysql


#   1. 连接MySQL 
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root123", charset='utf8', db='unicom', autocommit=True) # 表示当前电脑上的主机

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 进行收发数据, 指令

#   2. 发送指令(千万不要用字符串格式化去做SQL的拼接, 安全隐患SQL注入)
sql = "update admin set mobile=%s where id=%s" 
cursor.execute(sql, ["87777777777", 1, ]) 
conn.commit()


#   3. 关闭连接
cursor.close()
conn.close()