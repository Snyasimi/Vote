from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MyUsers

class MyUserCreationForm(UserCreationForm):
    

    class Meta:
        model = MyUsers
        fields = ('Name','Role_number','Dept_id','Email','password1','password2')



class Candidate_RegForm(forms.Form):
    Role_number = forms.CharField(max_length=50)
    Position = forms.CharField(max_length = 50)
    

 

