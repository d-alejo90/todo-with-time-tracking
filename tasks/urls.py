from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:id>', views.updateTask, name='update_task'),
    path('delete_task/<str:id>', views.deleteTask, name='delete_task'),
]