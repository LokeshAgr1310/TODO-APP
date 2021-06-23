from django.urls import path
from . import views
app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('add_todo', views.addTodo, name="add_todo"),
    path('delete_todo/<int:todo_id>/', views.deleteTodo, name="delete_todo"),
]