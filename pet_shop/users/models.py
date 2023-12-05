from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(blank=False,null=False,unique=True)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)