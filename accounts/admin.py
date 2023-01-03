from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUsers,Candidates,Departments
from django import forms

#USER INTERFACE ADM SITE

class AdminSiteConfig(BaseUserAdmin):

    list_display = ('Name','Role_number','Email','is_superuser','is_candidate')
    list_filter = ('is_superuser','is_candidate')
    seaech_fields = ('Name','Role_number')

    #What should display if you cick on a user in the admin site

    fieldsets = ((None,{'fields':('Name','Role_number','Dept_id',)}),

            ('Personal info',{'fields':('Email',)}),

            ('Permissions',{'fields':('is_superuser',)}),

            )


    #what displays if you want to add a user in the admin site
    add_fieldsets = (
            (None,{
                'classes':('wide',),
                'fields':('Name','Role_number','Dept_id','Email','is_candidate','Vote_status','password1','password2'),
                }
                
                ),
            )

    ordering = ("Name",)

    

class MyUserCreationForm(forms.ModelForm):
    password1= forms.CharField(label="password",widget=forms.PasswordInput)
    password2= forms.CharField(label="password Confirmation",widget=forms.PasswordInput)

    class Meta:
        model = MyUsers
        fields = ('Name','Role_number','Dept_id',)
        
   
# My models
admin.site.register(MyUsers,AdminSiteConfig)
admin.site.register(Candidates)

