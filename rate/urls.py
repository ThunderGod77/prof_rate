from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("prof/",views.prof,name="prof_info"),
    path("course/",views.course,name="course")
]