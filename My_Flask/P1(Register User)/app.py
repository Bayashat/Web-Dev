from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])  # 代表只支持GET请求
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else: 
        # 1.接受用户通过POST形式发送过来的数据
        print(request.form)

        user = request.form.get('username')
        pwd = request.form.get('pwd')
        gender = 'Male' if request.form.get('gender') == '1' else "Female"
        hobbys = request.form.getlist('hobby')
        city = request.form.get('city')
        more = request.form.get('more')
        print(user, pwd, gender, hobbys, city, more)
        # 将用户信息写入文件中实现注册, 写入到excel中实现注册, 写入数据库中实现注册

        # 2.给用户再返回结果
        return "注册成功"


# @app.route('/get/result', methods=['GET']) 
# def get_result():
#     # 1.接受用户通过GET形式发送过来的数据
#     print(request.args)
#     # 2.给用户再返回结果
#     return "注册成功"

# @app.route('/post/result', methods=['POST']) 
# def post_result():
#     # 1.接受用户通过POST形式发送过来的数据
#     print(request.form)

#     user = request.form.get('username')
#     pwd = request.form.get('pwd')
#     gender = 'Male' if request.form.get('gender') == '1' else "Female"
#     hobbys = request.form.getlist('hobby')
#     city = request.form.get('city')
#     more = request.form.get('more')
#     print(user, pwd, gender, hobbys, city, more)
#     # 将用户信息写入文件中实现注册, 写入到excel中实现注册, 写入数据库中实现注册

#     # 2.给用户再返回结果
#     return "注册成功"


@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        # print(request.form)
        user = request.form.get('username')
        pwd = request.form.get('pwd')
        print(user, pwd)
        return "审查中"

@app.route('/index', methods=['GET']) 
def index():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run()