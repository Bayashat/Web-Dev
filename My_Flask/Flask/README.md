#                                           Flask Web 框架使用
##                  0. 安装
* pip install flask

##					1. 返回模板
* 创建web.py文件
* from flask import Flask, render_template
* app = Flask(__name__)
* 创建url和函数的对应关系: @app.route("/show/info")
* 在其下面创建函数并返回
	- 字符串: return "Beeline KZ"
    - 模板: return render_template('index.html')  # 默认去当前项目目录的templates文件夹中找
* 可以创建多个函数, 模板等

##					2. 静态文件
* 都要放在static目录下