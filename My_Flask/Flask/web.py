from flask import Flask, render_template

app = Flask(__name__)


@app.route("/show/info")  # 创建了url和函数的对应关系
def index():
    # return "Beeline KZ"
    return render_template('index.html')  # 默认去当前项目目录的templates文件夹中找


@app.route("/get/news")
def get_news():
    return render_template('get_news.html')

@app.route("/goods/list")
def goods_list():
    return render_template('goods_list.html')

@app.route("/user/list")
def user_list():
    return render_template('user_list.html')

@app.route("/register")
def register():
    return render_template('register.html')    
    



if __name__ == '__main__':
    app.run()  # app.run(host="127.0.0.1", port="8000") 端口可以在这儿写
