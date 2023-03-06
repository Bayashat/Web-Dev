from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# from .models import UserInfo
from app01 import models  # 导入models文件

# from app01 import models
from app01.models import Department, UserInfo

##                          0. 返回字符串
def hello(request):
    return HttpResponse("Hello World")  # HttpResponse返回的是一个字符串


##                          4. 返回HTML模板
def users_list(request):
    # 默认去templates目录找Html文件
    return render(request, 'users_list.html')

##                          5. 静态文件
def static_demo(request):
    return render(request, "static_demo.html")

##                          6. 模板的继承
def extend(req):
    return render(req, 'sun.html', {"name": "Ikris"})

#                           7. 模板标签语法
def template_tag(request): 
    #   1) 变量: 
    context = {}
    context["name"] = "Bayashat"


    #   2) 列表:
    views_list = ["Django", "Python", "C++"]
    context["views_list"] = views_list

    #   3) 字典
    views_dic = {"name": "Jordan", "age": 28, 'salary': 999}
    context["views_dic"] = views_dic

    #   4) 列表套字典
    data_list = [
        {"name": "James", "salary": 999, "role": "CTO"},
        {"name": "Lorn", "salary": 15410, "role": "CEO"},
        {"name": "Seri", "salary": 100, "role": "secrity guard"}
    ]
    context["data_list"] = data_list

    #   5) if / else
    score = 89
    context["score"] = score

    #   6) empty list
    empty_list = []
    context["empty_list"] = empty_list

    #   7) 注意: 只能在一个字典里传值
    return render(request, 'template_tag.html', context)  # 返回HTML模板    也可以: {'n1': name}    


#                           8. 模板的'过滤器'
def filter(request):
    context = {}
    views_list = ["Django", "Python", "C++"]
    context["views_list"] = views_list

    context['score'] = 100
    return render(request, 'filter.html', context)


#                           P1-伪新闻网站
def news(req):
    # 1. 定义一些新闻, 从网络爬虫 
    # 向地址发送请求: 
    # 通过python代码发送网络请求需要第三方模块: (pip install requests)  这个跟django的不一样
    import requests
    res = requests.get("https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20230105&st=env")
    data_list = res.json()
    # print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


#                           9. 请求与响应
def request_and_response(request):
    # request 是一个对象, 封装了用户发送过来的所有请求相关数据(通过浏览器, 爬虫等)

    #   1) 获取请求方式 GET/POST
    print(request.method)  # GET

    #   2) 在URL上传递值:  /request_and_response/?n1=123&n2=999&n3=q
    print(request.GET)  # 获取参数: <QueryDict: {'n1': ['123'], 'n2': ['999'], 'n3': ['q]}>

    #   3) 在请求体中提交数据
    print(request.POST)

    #   4) [响应] HttpResponse("返回内容") : 将字符串内容返回给请求者

    #   5) [响应] 读取HTML的内容 + 渲染(替换) -> 生成字符串, 返回给用户浏览器
    # return render(request, 'request_and_response.html', {"country": "Kazakhstan"})

    #   6) [响应] 让浏览器重定向到其他的页面
    return redirect("https://www.google.com")


#                           P2-用户登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # 如果是POST请求, 获取用户提交的数据
    # print(request.POST)

    username = request.POST.get('user')
    password = request.POST.get('pwd')

    if username == 'root' and password == 'root123':
        # return HttpResponse("登录成功")
        # 用户登录成功, 返回页面
        return redirect("https://www.google.com/?hl=zh_CN")

    # return HttpResponse("登录失败")
    # 用户登录失败了 也应该返回登录页面, 让他重新登录
    return render(request, 'login.html', {'error_msg': "用户名或密码错误"})

#                           10. ORM-数据库操作

def orm(request):
    #   测试ORM操作表中的数据

    #           1) 新增数据 (insert into app01_department(title) values("销售部"))
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")

    # UserInfo.objects.create(username="Bayashat", password="123456", age=20, date_of_birth="2002-12-23")
    UserInfo.objects.create(username="Kyran", password="9464548", age=22)


    #           2) 删除数据
    # UserInfo.objects.filter(id=3).delete()  
    # Department.objects.all().delete()

    #           3) 获取数据
    #   3.1-获取符合条件的所有数据
    # [对象, 对象, 对象] 
    # data_list = UserInfo.objects.all()  # 会得到叫 queryset 类型的数据, 如果写了类方法, 就是类里的 __str__ 方法的内容
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id, obj.username, obj.password, obj.age)

    #   3.2-获取符合条件的第一条数据
    # data_list = UserInfo.objects.filter(id=1)  # 还是会得到一个里面放对象的queryset

    # row_obj = UserInfo.objects.filter(id=1).first()  # 直接得到queryset里的第一个对象
    # print(row_obj.id, row_obj.username, row_obj.password, row_obj.age)

    #           4) 更新数据:
    # UserInfo.objects.all().update(password="999")
    # UserInfo.objects.filter(id=2).update(age=25)
    # UserInfo.objects.filter(username="Loki").update(age=999)

    return HttpResponse("Success")



#                           P3 - 用户管理
#               1) 展示用户
def info_list(request):
    #   1. 获取数据库中所有的用户信息 
    data_list = UserInfo.objects.all()  #[对象, 对象, 对象, ]
    # print(data_list)

    #   2. 渲染, 返回给用户
    return render(request, 'info_list.html', {'data_list': data_list})

#               2) 添加用户
def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    
    # 如果是POST请求, 获取用户提交的数据
    # print(request.POST)

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    # 添加到数据库
    UserInfo.objects.create(username = user, password = pwd, age = age)

    # 自动跳转
    return info_list(request)  # or return redirect("http://127.0.0.1:8000/app01/info/list/") / return redirect("/app01/info/list/")

#               3) 删除用户
def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()

    return redirect("/app01/info/list")


#                           P4 - 员工管理系统
#               1.1) 展示部门列表
def depart_list(request):
    #   1. 去数据库中获取所有的部门列表[obj, obj, obj]
    queryset = Department.objects.all()

    return render(request, 'depart_list.html', {"data_list": queryset})

#               1.2) 添加部门
def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    # 获取用户post提交过来的数据
    title = request.POST.get('title')

    # 保存到数据库  
    Department.objects.create(title = title)

    # 重定向回部门列表
    return redirect("/app01/depart/list/")

#               1.3) 删除部门
def depart_delete(request):
    # 获取ID
    nid = request.GET.get("nid")
    # 删除
    Department.objects.filter(id=nid).delete()
    
    # 重定向回部门列表
    return redirect("/app01/depart/list/")

#               1.4) 编辑部门
# http://127.0.0.1:8000/app01/depart/3/edit/
def depart_edit(request, nid):
    if request.method == 'GET':
        # nid = request.GET.get("nid")
        # title = Department.objects.get(id=nid).title  # or Department.objects.filter(id=nid).first().title

        # 根据nid, 获取对应部门的数据
        title = Department.objects.get(id=nid).title    # or Department.objects.filter(id=nid).first().title
        return render(request, 'depart_edit.html', {"title": title})
    
    # 获取用户提交的标题
    title = request.POST.get('title')

    # 根据ID找到数据库中的数据并进行更新
    Department.objects.filter(id=nid).update(title=title)
    return redirect('/app01/depart/list/')

#               2.1) 展示员工列表
from app01.models import Employee_info

def user_list(request):
    #   1. 获取所有的员工列表[obj, obj, obj]
    queryset = Employee_info.objects.all()

    """ 
    用Python的语法获取数据
    for obj in queryset:
        print(obj.create_time.strftime("%Y-%m-%d"))  
        obj.gender  # 1 or 2
        obj.get_gender_display()  # get_字段名称_display(): 就能得到对应元组的文本: 男 or 女

        obj.depart_id # 获取的是存储的部门id: 1, 2 ...
        obj.depart  # 根据ID自动去关联的表中获取那一行数据的depart对象
        obj.depart.title  # 获取depart对象的title字段   """
    
    return render(request, 'user_list.html', {"data_list": queryset})


#               2.2) 添加员工(原始方法)
def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': Employee_info.gender_choices,  # 获取性别元组
            'depart_list': Department.objects.all()  # 获取所有部门信息
        }
        return render(request, 'user_add.html', context)
    #   获取用户的数据
    user = request.POST.get('user')
    password = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('account')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gender')
    department = request.POST.get('department')

    #   添加到数据库中
    Employee_info.objects.create(name=user, password = password, age = age, 
                                 gender = gender, account = account, 
                                 create_time = ctime, depart_id = department)
                                
    #   返回到用户列表页面
    return redirect('/app01/user/list')

#               2.3) 使用ModelForm实现 添加员工
from django import forms

class UserModelForm(forms.ModelForm):
    # 重写定制校验条件(类似限制长度等)
    name = forms.CharField(min_length=5)

    class Meta: 
        model = Employee_info
        fields = ['name', 'password', 'age', 'gender', 'account', 'create_time', 'depart']  # 需要显示的fields
        # widgets = {  # 加样式
        #     "name": forms.TextInput(attrs={"class":"form-control"}),
        #     "password": forms.TextInput(attrs={"class":"form-control"}),
        #     "age": forms.TextInput(attrs={"class":"form-control"})
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环找到所有的插件, 添加了class="form-control"
        for name, field in self.fields.items():
            if name == 'create_time':
                field.widget.input_type = 'date'
            # print(name, field)
            field.widget.attrs = {"class":"form-control", "placeholder": field.label}


def user_model_form_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})

    # 用户 POST 提交数据, 数据校验
    form = UserModelForm(data=request.POST)  # 逐一校验
    if form.is_valid():  # 校验成功
        # print(form.cleaned_data)  # 校验成功获取到的数据
        # 如果数据合法, 保存到数据库
        form.save()
        return redirect('/app01/user/list')
    # 校验失败(在页面上显示错误信息)
    # print(form.errors)  # 错误信息
    return render(request, 'user_model_form_add.html', {"form": form})  # 校验失败后的form已经有用户的数据了


def calc(request):
    get_params = request.GET.get
    a = int(get_params('a', default=10))
    b = int(get_params('b', default=20))
    return JsonResponse({'sum': a + b, 'product': a * b})


def user(request):
    user_list = models.UserInfo.objects.all()  # 代表userInfo数据表里所有的数据
    # print(user_list)  # <QuerySet [<Person: Bayashat 20>, <Person: Ernar 21>]>
    for user in user_list:
        print(user)   # Bayashat 20   Ernar 21

    return HttpResponse('Hello from django db')




# user_list = []


def receive(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'user': username, 'pwd': password}
        # user_list.append(temp)
        # 将数据保存到数据库
        models.UserInfo2.objects.create(user=username, pwd=password)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo2.objects.all()
    return render(request, 'receive.html', {'data': user_list})