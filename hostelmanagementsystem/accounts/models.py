from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Student(models.Model):
	boolChoice=(("M","Male"),("F","Female"))
	student_name = models.CharField(max_length=100)
	f_name =models.CharField(max_length=100)
	b_date=models.DateField(null='true')
	s_gender = models.CharField(max_length = 1,choices=boolChoice,null='true')
	mobile_no=models.CharField(max_length=10,null='true')
	branch=models.CharField(max_length=100)
	s_age=models.IntegerField(null='true')
	add_area=models.CharField(max_length=100,default=None)
	add_city=models.CharField(max_length=100,default=None)
	add_state=models.CharField(max_length=100,default=None)
	s_email=models.EmailField(max_length=100,null='true')
	s_sem=models.IntegerField(null='true')
	

class Notice(models.Model):
	notice_title=models.CharField(max_length=100)
	description_data=models.CharField(max_length=600)


class Payment(models.Model):
	p_year=models.IntegerField(null='true')
	p_amount=models.IntegerField(null='true')
	p_type=models.CharField(max_length=50)
	p_details=models.CharField(max_length=500)
	p_roomno=models.IntegerField(null='true')
	created_date = models.DateTimeField('date published')

class Addstudent(models.Model):
	s_name=models.CharField(max_length=50)
	s_surname=models.CharField(max_length=50)
	s_sem=models.IntegerField(null='true')
	s_branch=models.CharField(max_length=50)
	s_room=models.IntegerField(null='true')

	
















