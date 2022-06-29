from django.db import models

# Create your models here.

class Student(models.Model):
    s_name=models.CharField(max_length=255)
    s_address=models.CharField(max_length=255)
    s_age=models.IntegerField()
    s_gender=models.CharField(max_length=255)
    s_email=models.EmailField()
    s_jdate=models.DateField()
    s_qualification=models.CharField(max_length=255)
    s_pno=models.IntegerField()