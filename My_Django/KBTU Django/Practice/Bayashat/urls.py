from django.urls import path

from . import views

app_name = 'Bayashat'
urlpatterns = [
    path('Bayashat/index', views.index)
]