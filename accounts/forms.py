from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MyUsers

class MyUserCreationForm(UserCreationForm):
    

    class Meta:
        model = MyUsers
        fields = ('Name','Role_number','Dept_id','Email','password1','password2')



class VotingForm(ModelForm):
   # password1 = models.CharField(max_length=255)
    pass

 

