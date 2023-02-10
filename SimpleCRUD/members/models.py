from django.db import models

# Create your models here.
class Member(models.Model):
    userid = models.CharField(max_length=10, default="xxxxx")
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthday = models.DateField(default="1000-01-01")
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=255, null=True)
    joineddate = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
