from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    
    def __str__(self) -> str:
        return self.username

class Phone(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)
    phone_model = models.CharField(max_length=20)
    