from django.db import models

# Create your models here.

class user_signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class notes(models.Model):
    query=models.CharField(max_length=200)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to="MyFiles")
    comments=models.TextField()

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    sub=models.CharField(max_length=100)
    msg=models.TextField()