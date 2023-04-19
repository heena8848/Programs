from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('signin',views.signin, name="signin-user"),
    path('signup',views.signup, name="signup-user"),
    path('logout',views.logout_,name="logout-user"),
    path('dashboard',views.dashboard, name="dash-board"),
    path('list',views.get_list, name="get-list"),
    path('slider',views.showsliders, name="image-slider"),
    path('carausel',views.imageslider, name="image-slider")
]