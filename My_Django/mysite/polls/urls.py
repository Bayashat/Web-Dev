from django.urls import path
from django.contrib import admin
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

