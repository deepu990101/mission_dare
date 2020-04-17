
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.views.generic.base import View

from app_hrm.models import Employee2,Education_details
from app_hrm.forms import Educationform


def home(request):
    return render(request, "home.html")


def registration(request):
    return render(request, "registration.html")




def education(request):
    Emp_ID = request.POST["t1"]
    First_name = request.POST["t2"]
    Middle_name = request.POST["t3"]
    Last_name = request.POST["t4"]
    Father_name = request.POST["t5"]
    Mother_name = request.POST["t6"]
    Emp_DOB = request.POST["t7"]
    Emp_Temp_Address = request.POST["t8"]
    Emp_Perm_Address = request.POST["t9"]
    Gender = request.POST["t10"]
    contact_no = request.POST["t11"]
    aadhar_no = request.POST["t13"]
    pan_no = request.POST["t14"]
    image = request.POST["t12"]
    emp = Employee2(Emp_ID=Emp_ID, First_name=First_name, Middle_name=Middle_name, Last_name=Last_name,
                    Father_name=Father_name, Mother_name=Mother_name, Emp_DOB=Emp_DOB,
                    Emp_Temp_Address=Emp_Temp_Address, Emp_Perm_Address=Emp_Perm_Address, Gender=Gender,
                    contact_no=contact_no, image=image, aadhar_no=aadhar_no, pan_no=pan_no)
    emp.save()

    return render(request,"education2.html",{"data":Educationform()})

#

# def submit(request):
#
#     identity=request.POST["22"]
#     Tenth_marks_memo = request.POST["t15"]
#     Intermediate_marks_memo = request.POST["t16"]
#     Diploma1_marks_memo = request.POST["t17"]
#     Diploma2_marks_memo = request.POST["t18"]
#     Diploma3_marks_memo = request.POST["t19"]
#     Graduation_marks_memo = request.POST["t20"]
#     Post_Graduation_marks_memo = request.POST["t21"]
#
#
#
#     edu=Education_details(identity_no=identity,Tenth_marks_memo=Tenth_marks_memo,Intermediate_marks_memo=Intermediate_marks_memo,Diploma1_marks_memo=Diploma1_marks_memo,Diploma2_marks_memo=Diploma2_marks_memo,Diploma3_marks_memo=Diploma3_marks_memo,Graduation_marks_memo=Graduation_marks_memo,Post_Graduation_marks_memo=Post_Graduation_marks_memo)
#     edu.save()
#
#     return render (request,"registration.html",{"msg":"Details Saved"})


class formclass(View):
     def post(self,request):
        ef = Educationform(request.POST,request.FILES)
        if ef.is_valid():
            ef.save()

        return render(request,"registration.html",{'data':"successful"})

     #     Emp_ID = request.POST["t1"]
     #     First_name = request.POST["t2"]
     #     Middle_name = request.POST["t3"]
     #     Last_name = request.POST["t4"]
     #     Father_name = request.POST["t5"]
     #     Mother_name = request.POST["t6"]
     #     Emp_DOB = request.POST["t7"]
     #     Emp_Temp_Address = request.POST["t8"]
     #     Emp_Perm_Address = request.POST["t9"]
     #     Gender = request.POST["t10"]
     #     contact_no = request.POST["t11"]
     #     aadhar_no = request.POST["t13"]
     #     pan_no = request.POST["t14"]
     #     image = request.POST["t12"]
     #     emp = Employee2(Emp_ID=Emp_ID, First_name=First_name, Middle_name=Middle_name, Last_name=Last_name,
     #                     Father_name=Father_name, Mother_name=Mother_name, Emp_DOB=Emp_DOB,
     #                     Emp_Temp_Address=Emp_Temp_Address, Emp_Perm_Address=Emp_Perm_Address, Gender=Gender,
     #                     contact_no=contact_no, image=image, aadhar_no=aadhar_no, pan_no=pan_no)
     #     emp.save()
