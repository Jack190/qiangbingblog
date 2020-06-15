from django.db import models

#Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    author = models.CharField(max_length=16)
    content = models.TextField()
    order =models.CharField(max_length=255)
    summary =models.CharField(max_length=500)
    images= models.ImageField(upload_to='images/%Y/%m/%d', blank=True,null=True)
    hits=models.IntegerField(default=0)

class Site(models.Model):
    sitename = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    login = models.ImageField(upload_to='pic/login', blank=True,null=True)
    banner = models.ImageField(upload_to='pic/banner', blank=True,null=True)
    copyrightinfo = models.CharField(max_length=255)
    
class Topic(models.Model):
    sid =models.CharField(max_length=255)
    bigtopic=models.CharField(max_length=50)
    #time= models.DateTimeField()
#    content = models.FileField(upload_to='docfile/%Y/%m/%d', blank=True,null=True)

class Admin(models.Model):
    admin_name = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=255)
    
class Member(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)