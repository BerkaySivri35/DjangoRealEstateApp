from django.urls import path

from . import views

urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('register', views.user_register, name='user_register'),
    path('logout', views.user_logout, name='user_logout'),
    path('dashboard', views.user_dashboard, name='user_dashboard'),
]