import pymysql


while True:  # 不停的输入值
    user = input("enter the username: ")
    if user.upper() == 'Q':     # 设置一个终止条件
        break
    pwd = input("enter the password: ")
    mobile = input("enter the phone number: ")

    #   1. 连接MySQL 
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root123", charset='utf8', db='unicom', autocommit=True) # 表示当前电脑上的主机

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 创建游标, 用来 进行收发数据, 指令

    #   2. 发送指令 (千万不要用字符串格式化去做SQL的拼接, 安全隐患SQL注入)
    sql = "insert into admin(username,password,mobile) values(%s, %s, %s)"  # 写这样也可以, 但之后要写字典, 而不是列表: values(%(n1)s, %(n2)s, %(n3)s)
    cursor.execute(sql, [user, pwd, mobile])  # ['Bayashat', 'qwe123', '87078788883'] or {"n1": "Bayashat", "n2": "qwe123", "n3": "87078788883"}
    # conn.commit()  # 是用来提交的.  当数据库名字后没有写autocommit时需要写这个

    #   3. 关闭连接
    cursor.close()
    conn.close()


    