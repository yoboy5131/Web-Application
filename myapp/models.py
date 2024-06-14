# myapp/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Admission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField(default="")
    nationality = models.CharField(default = "" ,max_length=60)
    gender = models.CharField(default = " ", max_length=10)
    emergency_name = models.CharField(max_length=100, default ="")
    emergency_phone = models.IntegerField( default="")
    emergency_email = models.EmailField(default="")
    id_mark=models.TextField(default="")
    b_group =models.TextField(default="")
    identity_mark=models.CharField(default="",max_length=100)
    date_admission=models.DateField()
    prefer_lan=models.CharField(default="",max_length=20)
    father_occu = models.CharField(default="",max_length=30)
    mother_occu = models.CharField(default="", max_length=30)
    income= models.IntegerField(default="")
    extra_activities = models.CharField(default="",max_length=100)
    photo = models.ImageField(default="",blank= True)
    proof_address= models.FileField(default="",blank= True)
    identity = models.FileField(default="",blank= True)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'