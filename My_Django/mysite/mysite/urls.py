from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from app01 import views

urlpatterns = [  # url和视图函数的对应关系
    path('admin/', admin.site.urls),
    path('app01/', include('app01.urls')),
    path('polls/', include('polls.urls')),
]
