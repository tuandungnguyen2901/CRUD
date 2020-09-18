from django.db import models


class Position(models.Model):
    tittle = models.CharField(max_length=50)

    def __str__(self):
        return self.tittle


# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)