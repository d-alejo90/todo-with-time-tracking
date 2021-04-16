from django.urls import path
from . import views

urlpatterns = [
    path('auth/register', views.register, name='register'),
    path('auth/signin', views.signin, name='signin'),
    path('logout/', views.logout, name='logout')
]