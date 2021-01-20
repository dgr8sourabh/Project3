from django.db import models

# Create your models here.


class EmployeeModel(models.Model):

    idno = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=30)


    def __str__(self):
        return self.name


class Emp_Department(models.Model):
    dep_id =models.IntegerField()
    dep_name = models.CharField(max_length=50)
