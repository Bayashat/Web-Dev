from django.contrib import admin
from django.urls import path
from app01 import views  # or from . import views

# url和视图函数的对应关系
urlpatterns = [  
    path('admin/', admin.site.urls),
    # url('^$', views.Hello),
    path('hello/', views.hello),    # 0. 返回字符串
    path('template/users_list/', views.users_list),    # 4. 返回HTML模板
    path('template/static_demo/', views.static_demo),    # 5. 静态文件
    path('template/extended/', views.extend),    # 6. 模板的继承
    path('template/template_tag/', views.template_tag),  # 7. 模板标签语法
    path('template/filter/', views.filter),   # 8. 模板的'过滤器'
    path('p/news/', views.news),  # P1-伪新闻网站
    path('request_and_response/', views.request_and_response),  # 9. 请求与响应
    path('p/login/', views.login),    # P2-用户登录
    path('orm/', views.orm),    # 10. ORM - 数据库操作
    path('info/list/', views.info_list),    # P3-用户管理  1)展示用户
    path('info/add/', views.info_add),    # P3-用户管理  2)添加用户
    path('info/delete/', views.info_delete),    # P3-用户管理  3)删除用户

    #       1) 部门管理
    path('depart/list/', views.depart_list),  # P4-员工管理系统  1.1) 展示部门列表
    path('depart/add/', views.depart_add),  # P4-员工管理系统  1.2) 添加部门
    path('depart/delete/', views.depart_delete),  # P4-员工管理系统  1.3) 删除部门

    # http://127.0.0.1:8000/app01/depart/3/edit/    必须传一个整型数字
    path('depart/<int:nid>/edit/', views.depart_edit),  # P4-员工管理系统  1.4) 编辑部门

    #       2) 员工管理
    path('user/list/', views.user_list),  # P4-员工管理系统  2.1) 展示员工列表
    path('user/add/', views.user_add),  # P4-员工管理系统  2.2) 添加员工
    path('user/model/form/add/', views.user_model_form_add),  # P4-员工管理系统  2.3) 使用 ModelForm 添加员工

    path('receive/', views.receive),
    path('api/calc', views.calc),
    path('api/database', views.user),
]
