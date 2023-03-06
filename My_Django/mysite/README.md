# Djnago version: 3.2.16

## 官方文档: https://docs.djangoproject.com/zh-hans/3.2/

##                  				1.安装Django:
    1. 
      	- 在cmd: pip install django / py -m pip install Django
    	- 或者在Pycharm安装
    2. 查看版本: py -m django --version
	3. 设置环境变量: 
		- 找到Django的安装路径: pip show django, 在 python 解释器目录下的Scripts目录里有django-admin.exe 
		- 进入环境变量新增这个路径
	3. 在cmd输入 django-admin help 以检测是否成功

	c:\python311
		- python.exe
		- Scripts
			- pip.exe
			- django-admin.exe 	[工具, 创建django项目中的文件和文件夹]
		- Lib
			- 内置模块
			- site-packages
				- openpyxl
				- python-docx
				- flask
				- django		[框架的源码]

##                  				2.创建项目:
    django-admin startproject [项目名]

### 	2.1) 默认项目的文件介绍:
	* 可以看到Django自动帮我们创建了一个mysite文件夹, 这是项目的根目录. mysite根目录中, 又有一个mysite目录, 这是整个项目的配置文件目录
		(一定不要和同名的根目录混淆)
	* manage.py: 它是整个项目的管理脚本. [项目的管理, 启动项目, 创建app, 数据管理]
	* 在配置文件目录下: 
		__init__.py: 一个空文件, 告诉 Python 这个目录应该被认为是一个 Python 包
		settings.py: [项目配置文件] [可用于连接数据库, 注册app等]
		urls.py: Django 项目的 URL 声明, 就像你网站的“目录”, [URL和函数的对应关系][***常操作的文件***]
		asgi.py 和 wsgi.py: [接收网络请求的]

### 	2.2) 运行项目: 
    运行 py manage.py runserver [可指定端口] , Django会以127.0.0.1:8000这个默认配置启动开发服务器


##                  				3. APP
* 项目: 
	- app: 用户管理 
	- app: 订单管理
	- app: 后台管理
	- app: 网站
	- app: API
* 各个app都有各自独立的[表结构, 函数, HTML模板, CSS]

* 注意: 我们开发比较简洁, 用不到多app, 一般情况下, 项目下创建一个app即可
### 	3.1) 创建app:
*	py manage.py startapp "APP名字"
### 	3.2） 注册app:
*	在settings.py 里 INSTALLED_APPS里填入 'app名.apps.app名Config'
  
##                  				4. 返回 HTML 模板
* 返回模板需要在指定app里创建templates目录, 里面填入所需html文件. 再通过在views.py里返回render(request, "HTML模板名"), 最后改urls里即可

###			1) 编写URL和视图函数的对应关系(urls.py)
* url里写 path('index/', views.index)  'index/' 是URL路由, views.index 是views.py里的index 视图函数

###			2) 编写视图函数(views.py)
* 创建函数index(request), 默认需要一个参数. 可以先返回 HttpResponse("Welcome")
* 当用户访问 index/ 这个URL时, 就会显示 "Welcome" 这个字符串 

* 默认会根据app的注册顺序, 逐一去它们的templates目录找
	- 如果在settings.py里的 TEMPLATES列表里的字典里写了 'DIRS': [os.path.join(BASE_DIR, 'templates')],  (需要import os) , 那优先会在根目录下的templates里找


##                  				5. 静态文件
* 在static_demo.html 和 mysite/app01/views.py 下的 static_demo 函数实现

1. 在开发过程中, 一般将 Img, CSS, JS 都会当作静态文件处理
2. 必须在app里创建static文件夹, 里面创建 img, css, js,plugins 文件夹, 各自放静态文件. plugins里放插件(bootstrap, jQuery)
3. 推荐使用 {% load static %} 语法: "{% static 'app01/img/girl.jpg' %}"



##                 					6. 模板的继承
* 在sun.html, father.html 和 mysite/app01/views.py 下的 extend 函数实现

* 概念: 公用部分放到父类, 子类继承这些部分, 子类也会有自己相应的部分


##                 					7. 模板标签语法
* 在template_tag.html 和 mysite/app01/views.py 下的 template_tag 函数实现

* 本质上: 在HTML中写一些占位符, 由数据对这些占位符进行替换和处理


##                 					8. 模板的 过滤器
* 在filter.html 和 mysite/app01/views.py 下的 filter 函数实现

* 作用是: 将数据显示在网页之前做一些"过滤"处理


##                  				Practice-1: 伪新闻-通过python网络爬虫将数据放入模板, 并返回页面
* 在news.html 和 mysite/app01/views.py 下的 news函数实现


##      6.1 模板的继承
* 在father.html 和 son.html 和 mysite/app01/views.py 下的 extend 函数实现

##                  				9. 请求和响应 / request and response
* 在 request_and_response.html 和 mysite/app01/views.py 下的 request_and_response 函数实现


##                  				Practice-2: 用户登录
* 在login.html 和 mysite/app01/views.py 下的 login 函数实现

##                  				10. 数据库操作 / ORM
* Django开发操作数据库更简单, 内部提供了ORM框架, 起到了翻译的过程
* Django 默认使用轻量级sqlite数据库
* 使用数据库首先要注册app

* 安装第三方模块: pip install mysqlclient (用来连接数据库)

###		1) ORM介绍
* ORM可以帮助我们做两件事: 
	- 创建, 修改, 删除数据库中的表(不用写SQL语句) [但是无法创建数据库]
	- 操作表中的数据 (不用写SQL语句)
		insert into...
		update ....
		select ...

###		2) 配置数据库
1. 在settings中，配置数据库相关的参数，如果使用sqlite3，则不需要做任何修改
* [sqlite3]: 
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.sqlite3',
		}
	}

* [MySQL]: 
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'dbname',  # 数据库名字
			'USER': 'root', 
			'PASSWORD': 'xxx',
			'HOST': '127.0.0.1',  # localhost  MySQL安装在哪台服务器地址
			'PORT': 3306,  # 端口
		}
	}

###		4.1) django操作表-MySQL
* 创建表
* 删除表
* 修改表
	1) 在models.py文件里, 写表和数据

		from django.db import models

		class UserInfo(models.Model): 要继承这个类,固定写法
			username = models.CharField(max_length=32)
			password = models.CharField(max_length=32)
			int = models.IntegerField()
	* 表名会是 app名_类名, 表里的每一行都是表的每一列数据

	2) 执行命令以迁移数据到数据库: 
	py manage.py makemigrations     这会在app目录中的migrations目录中生成一个0001_initial.py迁移记录文件。
	py manage.py migrate      这样,我们就在数据库中将所有app的数据表都创建好了

	3) 注意: 
		- 在表中新增列时, 由于已存在列中可能已有数据, 所以新增列必须要指定对应的数据
			1. 手动输入一个值
			2. 设置默认值: age = models.IntegerField(default=2)
			3. 允许为空: last_login_time = models.DateField(null=True, blank=True)
	4) 直接添加类和类字段,或删除类或类字段, 以添加,删除 数据表和数据


###		4.2) django操作表-Sqlite3

1) 通过DB Browser:
	- 创建表
	- 删除表
	- 修改表 
		在 app01/models.py 文件里,写表和数据

		from django.db import models

		class UserInfo(models.Model): 要继承这个类,固定写法
			username = models.CharField(max_length=32)
			password = models.CharField(max_length=32)
			int = models.IntegerField()
	* 表名会是 app名_类名, 表里的每一行都是表的每一列数据

2) 安装好Pillow: 
	- python -m pip install Pillow

3) 执行命令以迁移数据到数据库: 
	py manage.py makemigrations     这会在app目录中的migrations目录中生成一个0001_initial.py迁移记录文件。
	py manage.py migrate      这样,我们就在数据库中将所有app的数据表都创建好了. 我们可以看到项目根目录下出现了一个db.sqlite3文件

4） 通过admin panel 添加,删除,修改表:
	1.首先创建超级用户(superuser):
		- python manage.py createsuperuser
		- 填用户名,邮箱,密码
		- 在app填入了数据表的app目录下的admin.py: 
			from django.contrib import admin

			from .models import Product, ProductCategory	导入数据库名

			admin.site.register(Product)
			admin.site.register(ProductCategory)
	2.通过http://127.0.0.1:8000/admin/ 访问 admin panel 
	3. 直接点击选择相应的数据库进行操作


5) 链接数据库
* sqlite3:
	1) 可以通过DB Browser: 安装DB Browser, 打开 db.sqlite3 文件
	2) 通过web 版本的 sqliteviewer.app 查看 db.sqlite3 文件


##                  				Practice-3: 用户管理
1. 在mysite/app01/models.py 里写了 Department, User_info 类 
2. 在 mysite/app01/views.py 下的 info_list, info_add, info_delete 函数实现

##                  				Practice-4: 员工管理系统
1. 在mysite/app01/models.py 里写了 Department, Employee_info 类 
2. 在mysite/app01/urls.py 里配置了路由
3. 在 mysite/app01/views.py 下的 depart_list, depart_add, depart_delete, depart_edit, 函数实现 部门管理
4. 在 mysite/app01/views.py 下的 user_list, user_add 实现员工管理

* 实现了部门管理 和 员工管理的页面
* 	1) 都先使用了原始方式思路 (本质: 麻烦)
		- 用户提交的数据没有校验
		- 如果有错误, 应该有错误提示
		- 页面上, 每一个字段都要手写(name, pwd, age...)
		- 关联的数据, 需要手动获取并展示在页面
	2) Django 组件
	* Form 组件(小简便)
	* ModelForm组件(最简便)



##                  				11. ModelForm 组件 & P4-员工管理系统
1. 在mysite/app01/models.py 里写了 Department, Employee_info 类 
2. 在 Department 类中添加了__str__ 
3. 在原先的 user/list 里添加里 "添加用户 Model Form"按钮, 跳转至 user/model/form/add
4. 添加了 UserModelForm 类, 在里面直接关联了 models.py 里的类
5. 在 mysite/app01/views.py 下的 user_model_form_add 函数实现
 



##                  	9. 自定义用户模型
* 在app下的models.py里:
	from django.db import models
	from django.contrib.auth.models import AbstractUser

	class User(AbstractUser):  创建了类
		image = models.ImageField(upload_to='users_images', null=True, blank=True)

