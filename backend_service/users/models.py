from django.db import models

class Users(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField()
    is_seller=models.BooleanField()
    
