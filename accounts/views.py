from django.shortcuts import render
from .forms import MyUserCreationForm
from .models import MyUsers,MyUserManager
# Create your views here.

def register(request):

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()




    else:

        context = {'form':MyUserCreationForm()}

    return(render(request,"accounts/reg.html",context))
