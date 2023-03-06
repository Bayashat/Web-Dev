#                                       SQL 学习
##                              0.下载安装
* 	1) 下载链接:
		- MySQL: https://downloads.mysql.com/archives/community/   推荐5.7版本
*   2) 安装补丁:	
        1. vcredist_x64.exe: https://learn.microsoft.com/zh-cn/cpp/windows/latest-supported-vc-redist?view=msvc-170
     	2. dxwebsetup.exe: https://www.microsoft.com/zh-CN/download/details.aspx?id=35
*   3) 安装:
        - mysql-5.7.31-winx64 是免安装的版本
        - 解压zip文件
        - 将解压后的文件夹放入路径(不要有中文路径), 推荐路径: C:\Program Files\mysql-5.7.31-winx64	
		- 可通过 "where mysql" 查看存在路径
*   4) 创建配置文件:
	    - 在安装目录下创建 "my.ini" ,填入:
			[mysqld]
			# port
			port=3306

			# set basedir to your installation path
			basedir=C:\\Program Files\\mysql-5.7.31-winx64

			# set datadir to the location of your data directory
			datadir=C:\\Program Files\\mysql-5.7.31-winx64\\data

* 	5) 初始化
	- 打开终端 & 以管理员的权限去运行(搜索框输入cmd, 选择"以管理员身份运行")
	- 输入初始化的命令:
  		"C:\Program Files\mysql-5.7.31-winx64\bin\mysqld.exe"  --initialize-insecure
	- 安装目录下出现data文件夹即成功

##                              	1. 启动MySQL
* 启动MySQL一般有两种方式: 
	- 临时启动(不建议):
      - >>> "C:\Program Files\mysql-5.7.31-winx64\bin\mysqld.exe" 运行这个文件 会卡住, mysql就开启了. 关闭musql就关闭了
	- 永久启动(制作成Windows服务, 服务来进行关闭和开启)
      	1. 制作服务:
            >>> "C:\Program Files\mysql-5.7.31-winx64\bin\mysqld.exe" --install mysql57
	  	2. 启动服务:
    		>>> net start mysql57
	  	3. 关闭服务:
    		>>> net stop mysql57

##                              	2. 连接测试
* bin目录下mysql.exe就是自带连接MySQL的工具(客户端)

* 输入此命令以连接数据库: 
	>>> "C:\Program Files\mysql-5.7.31-winx64\bin\mysql.exe" -h 127.0.0.1 -P 3306 -u root -p  

	-h 127.0.0.1是IP, -P 3306是端口, -u root是用户, -p是密码

* 可以省略IP和端口
* 或者也可以将路径添加到环境变量后再直接省略写: mysql -u root -p    注意服务要开启

##                              	3. 设置密码
* set password = password('root123');

##									4. 查看已有的数据库(文件夹)
* show databases;
* exit; 退出数据库

##									5. 再连接MySQL
* 输入: mysql -u root -p
* Enter password: root123

##									6. 忘记密码怎么办?!
1. 关闭mysql服务
2. 修改mysql配置 重新启动mysql: mysql -u -root -p
3. 重新设置密码，再重新修改配置文件: 将skip-grant-tables=1 添加到 my.ini
4. 重新启动mysql服务
5. mysql -u -root -p
6. use mysql;
7. update user set authentication_string=password('新密码'), password_last_changed=now() where user=‘root’;
8. 重新修改配置文件回原样
————————————————
版权声明：本文为CSDN博主「虾条条条」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Shrimp_Code/article/details/125733173

##									7. MySQL指令
		MySQL:				认知:
		数据库			   文件夹
		数据表			    文件

###				1) 数据库管理(文件夹)
* (1)查看已有的数据库(文件夹):
	>>> show databases;
* (2)创建数据库:
	>>> create database 数据库名字;
	>>> create database 数据库名字 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
* (3)删除数据库:
 	>>> drop database 数据库名;
* (4)进入数据库:
	>>> use 数据库名字;
* (5)查看文件夹下所有数据表(文件):
	>>> show tables; 
  
###				2) 数据表管理(文件)
* 	(1) 创建表:
create table 表名称(
	列名称 类型,
	列名称 类型,
	列名称 类型
  )default charset=utf8;

create table tb1(
	id int auto_increment primary key,				-- 主键(不允许为空, 不允许重复)  
	name varchar(16) not null,		-- 不允许为空
	age int null,					-- 允许为空(默认)
	address varchar(32)	default 3	-- 插入数据时, address列的值默认为3
  )default charset=utf8;

* primary key: 主键一般用于表示当前行的数据的编号(类似于人的身份证)
* auto_increment: 内部维护自增

*   (2) 展示表的细节: 
>>> desc tb1;
* 	(3) 删除表:
>>> drop table 表名称;

#
###				3) 常用数据类型
* tinyint(unsigned)
	- 有符号(默认): -128 ~ 127
    - 无符号(需要加unsigned): 0 ~ 255
    - 1 byte storage
* int
	- 有符号: -2147483648 ~ 2147483647
  	- 无符号: 0 ~ 4294967295
    - 4 byte
* bigint
	- 有符号: -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
    - 8 byte
  
	# 创建表
	create table tb2(
		id bigint auto_increment primary key,
		salary int,
		age tinyint
	)default charset=utf8;
	# 插入数据
	insert into tb2(salary, age) values(10000,18);
	insert into tb2(salary, age) values(20000,28),(30000,38);
	
	# 查看表中的数据
	select * from tb2

* float
	- 存储不是特别精准
* double
* decimal
	- 准确的小数值, m是数字总个数(负号不算), d是小数点后个数. m最大值为65, d最大值为30
    - salary decimal(8,2);	-- (m,d)
    create table tb3(
        id bigint auto_increment primary key,
        salary decimal(8,2)  -四舍五入的情况
    )default charset=utf8;
  	insert into tb3（salary) values(1.288),(4.862),(3.156);   -- 1.29, 4.86, 3.16

###				4) 字符串类型
* char(m)
	- m代表字符串的长度, 最多可容纳 255 个字符
    - 查询的速度快 11^5
    - 定长字符串
        mobile char(11)  -- 固定字符串长度, 没有11也按11个存
 * varchar(m)
	- m代表字符串的长度, 最多可容纳 65535字节/3 = 最大的m
	- 变长字符串: 真实字符串多长就按多长存储
	- 节省空间
   	mobile varchar(11)
* text
	- text数据类型用于保存变长的大字符串, 可以组多到65535 / (2**16 - 1) 个字符
    - 一般情况下, 长文本会用text类型. 例如: 文章, 新闻等.
* mediumtext
	- 2**24 - 1
* longtext
	- 2**32 - 1

###				5) 时间字符串
* datetime
	- YYYY-MM-DD HH:MM:SS   例如: (1000-01-01 00:00:00 / 9999-12-31 23:59:59)
* date
	- YYYY-MM-DD (1000-01-01 / 9999-12-31) 

    create table tb4(
        id int auto_increment primary key,
        name varchar(64) not null,
		password char(64) not null,
		email varchar(64) not null,
		age tinyint,
		salary decimal(10,2),
		ctime datetime
    )default charset=utf8;
	insert into tb4(name,password,email,age,salary,ctime) values("Bayashat","123",'xx@live.com',20,1000.20,"2023-01-25 00:08:24");

##									8.数据行操作
###				1) 新增数据 
>>> insert into 表名(列名,列名) values(值,值);
>>> insert into 表名(列名,列名) values(值,值),(值,值),(值,值);		插入多行数据

>>> insert into tb4(name,password,email,age,salary,ctime) values('Bayashat','456','fal@live.com',21,999.154,"2023-01-25 22:35:04");

###				2) 删除数据
>>> delete from 表名;
>>> delete from 表名 where 条件;

>>> delete from tb4;
>>> delete from tb4 where id = 2 and name = "Kyran";
>>> delete from tb4 where id = 2 or name = "Kyran";
>>> delete from tb4 where id > 4;
>>> delete from tb4 where id >= 4;
>>> delete from tb4 where id != 4;
>>> delete from tb4 where id in (1,5);

###				3) 修改数据 
>>> update 表名 set 列=值
>>> update 表名 set 列=值, 列=值
>>> update 表名 set 列=值 where 条件;

>>> update tb4 set password='xaxaxa';  修改表里所有的密码为xaxaxa
>>> update tb4 set email='xaxaxa' where id > 5; 
>>> update tb4 set age=age+10 where id > 5;

###				4) 查询数据
>>> select * from 表名称
>>> select 列名称, 列名称 from 表名称; 
>>> select 列名称, 列名称 from 表名称 where 条件; 

>>> select id, name from tb4;
>>> select id, name from tb4 where id > 3;
>>> select id, name from tb4 where name="xx" and password="xx";

##									9.小结
* 我们平时开发系统时, 一般情况下: 
	- 创建数据库
	- 创建表结构
都是需要提前通过工具+命令创建
* 但是, 表中的数据一般情况下都是通过程序来实现增删改查.


##									Practice-1: 员工管理
### 	1) 要求: 
* 使用MySQL内置工具(命令)
	- 创建数据库: unicom
	- 创建一张表: admin
		表名: admin
		列: 
			id, 整型, 自增, 主键,
			username 字符串 不为空,
			password 字符串 不为空,
			mobile 字符串 不为空

* Python代码实现: 	
	- 添加用户
	- 删除用户
	- 查看用户
	- 更新用户信息

### 	2) 实现 MySQL指令: 
1) create database unicom DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
2) use unicom;
3) 
create table admin(
	id int auto_increment primary key,
	username varchar(32) not null,
	password varchar(32) not null,
	mobile char(11) not null
) default charset=utf8;

###		3) Python操作MySQL: 用Python代码连接MySQL并发送指令
* 默认是不可以的, 需要安装第三方模块:
	- pip install pymysql

1) 创建数据
2) 查询数据
3) 删除数据
4) 修改数据

###		强调: 
* 在进行 新增, 删除, 修改时, 一定要记得commit, 不然数据库没有数据
	cursor.execute("...")
	conn.commit()
* 在查询时, 不需要commit, 执行fetchall/fetchone
	cursor.execute("...")

	- 第一条数据, 字典, 无数据时是None
	v1 = cursor.fetchone()

	- 所有数据, 列表里套字典  没数据就是: 空列表
	v2 = cursor.fetchall()
	
* 对于SQL语句不要用Python的字符串格式化进行拼接(会被SQL注入), 一定要用execute + 参数	
	cursor.execute(".%s....%s", ["xx", "xx"])