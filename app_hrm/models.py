from django.db import models
import datetime
class Employee(models.Model):
    Emp_ID = models.CharField(primary_key=True,unique=True,max_length=10)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=10)
    Last_name = models.CharField(max_length=10)
    Father_name = models.CharField(max_length=20)
    Mother_name = models.CharField(max_length=20)
    Emp_DOB = models.DateField()
    Emp_Temp_Address = models.TextField(blank=True,)
    Emp_Perm_Address = models.TextField(blank=True,)
    Gender = models.CharField(max_length=10,)
    contact_no = models.IntegerField(unique=True)
    aadhar_no = models.IntegerField()
    pan_no = models.CharField(max_length=10,)
    image = models.ImageField(upload_to='emp_images/',)

class Employee2(models.Model):
    Emp_ID = models.CharField(primary_key=True,max_length=10)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=10)
    Last_name = models.CharField(max_length=10)
    Father_name = models.CharField(max_length=20)
    Mother_name = models.CharField(max_length=20)
    Emp_DOB = models.DateField()
    Emp_Temp_Address = models.TextField(blank=True,)
    Emp_Perm_Address = models.TextField(blank=True,)
    Gender = models.CharField(max_length=10,)
    contact_no = models.IntegerField(unique=True)
    aadhar_no = models.IntegerField(unique=True)
    pan_no = models.CharField(max_length=10,unique=True)
    image = models.ImageField(upload_to='emp_images/',unique=True)
    def __str__(self):
        return self.Emp_ID



class Education_details(models.Model):
    identity_no = models.OneToOneField(Employee2,on_delete=models.CASCADE,)
    Tenth_marks_memo = models.FileField(upload_to='Tenth_marks_memo/',unique=True)
    Intermediate_marks_memo = models.FileField(upload_to='Intermediate_marks_memo/',unique=True)
    Diploma1_marks_memo= models.FileField(upload_to='Diploma1_marks_memo/',unique=True)
    Diploma2_marks_memo = models.FileField(upload_to='Diploma2_marks_memo/',unique=True)
    Diploma3_marks_memo = models.FileField(upload_to='Diploma3_marks_memo/',unique=True)
    Graduation_marks_memo = models.FileField(upload_to='graduation_marks_memo/',unique=True)
    Post_Graduation_marks_memo = models.FileField(upload_to='postgraduation_marks_memo/',unique=True)


