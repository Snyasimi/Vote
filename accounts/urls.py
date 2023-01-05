from django.urls import path,include
from . import views

app_name="accounts"
urlpatterns = [
        path("",views.register,name="register"),
        path("",views.Register_candidate,name = "Reg_candidate"),

        ]

