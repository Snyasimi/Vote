from django.urls import path,include
from . import views

app_name="accounts"
urlpatterns = [
        path("",views.register,name="register"),
        path("register-candidates",views.Register_candidate,name = "Reg_candidate"),
        path("View-candidates",views.CandidateView.as_view(),name="view-candidates"),

        ]

