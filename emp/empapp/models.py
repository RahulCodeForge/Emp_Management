from django.db import models

# Create your models here.


class Department(models.Model):
    dname =models.CharField(max_length=100,null=False)
    dloc = models.CharField(max_length=100)


class Role(models.Model):
    rname=models.CharField(max_length=100)

class Employee(models.Model):

    ename=models.CharField(max_length=100,null=False)
    dept =models.ForeignKey(Department,on_delete=models.CASCADE)
    salary =models.IntegerField(default=0)
    bonus =models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    Phone = models.IntegerField(default=0)
    hiredate=models.DateField()
    