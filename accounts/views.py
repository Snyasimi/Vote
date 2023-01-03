from django.shortcuts import render
from .forms import MyUserCreationForm
from .models import MyUsers,MyUserManager
# Create your views here.

def register(request):

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:

                new_user = MyUsers.objects.create_user(

                        form.cleaned_data['Role_number'],
                        form.cleaned_data["Name"],
                        form.cleaned_data['Email'],
                        form.cleaned_data["Dept_id"],
                        password2

                        )
                new_user.save()




    else:

        context = {'form':MyUserCreationForm()}

    return(render(request,"accounts/reg.html",context))
