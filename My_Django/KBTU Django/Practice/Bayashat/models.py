from django.db import models
import datetime

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=32)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Dish(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(to=MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name} | {self.price}"

class Order(models.Model):
    client_name = models.CharField(max_length=32)
    date_ordered = models.DateField(default=datetime.date.today)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(to=Dish, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.client_name} | {self.dish}"
