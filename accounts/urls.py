from django.urls import path,include
from . import views

app_name="accounts"
urlpatterns = [
        path("",views.CreateUser.as_view(),name="register"),
        path("register-candidates",views.CreateCandidate.as_view(),name = "Reg_candidate"),
        path("View-candidates",views.CandidateView.as_view(),name="view-candidates"),
        ]

