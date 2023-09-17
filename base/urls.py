from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepageNew, name='homeNew'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    
    
]
