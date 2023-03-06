from django.contrib import admin

# Register your models here.
from .models import Restaurant, MenuCategory, Dish, Order

admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(Dish)
admin.site.register(Order)
