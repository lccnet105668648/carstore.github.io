# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)  # 確認新增的字段

    def __str__(self):
        return f'{self.user.username} - {self.car.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

