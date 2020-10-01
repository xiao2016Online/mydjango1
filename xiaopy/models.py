from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36, null=False, default='')
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100, null=True, blank=True)
    createdTime = models.DateTimeField(auto_now_add=True, null=True, )
    sex = models.BooleanField(default=False)



