from django.db import models

# Create your models here.


class Department(models.Model):
    dname =models.CharField(max_length=100,null=False)
    dloc = models.CharField(max_length=100)

    def __str__(self):

        return f'{self.dname},{self.dloc}'


class Role(models.Model):
    rname=models.CharField(max_length=100)
    
    def __str__(self):

        return f'{self.rname}'

class Employee(models.Model):

    ename=models.CharField(max_length=100,null=False)
    dept =models.ForeignKey(Department,on_delete=models.CASCADE)
    salary =models.IntegerField(default=0)
    bonus =models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    Phone = models.IntegerField(default=0)
    hiredate=models.DateField()
    
    def __str__(self):

        return f'{self.ename},{self.dept},{self.salary},{self.role},{self.Phone},{self.hiredate}'