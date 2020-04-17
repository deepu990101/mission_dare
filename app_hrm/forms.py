from django import forms
from app_hrm.models import Education_details



class Educationform(forms.ModelForm):
    class Meta:
        model = Education_details
        fields = '__all__'



    # Tenth_marks_memo = forms.FileField()
    # Intermediate_marks_memo = forms.FileField()
    # Diploma1_marks_memo= forms.FileField()
    # Diploma2_marks_memo = forms.FileField()
    # Diploma3_marks_memo = forms.FileField()
    # Graduation_marks_memo = forms.FileField()
    # Post_Graduation_marks_memo = forms.FileField()