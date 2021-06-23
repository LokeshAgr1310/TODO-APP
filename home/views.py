from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from django.urls import reverse
from django.utils import timezone

# Create your views here.

def index(request):
    todo_list = Todo.objects.all().order_by('-date_added')
    context = {"todos_list": todo_list}
    return render(request, 'home/index.html', context)


def addTodo(request):
    input_title = request.POST.get('title')
    input_text = request.POST.get('content')
    current_date = timezone.now()
    Todo.objects.create(title=input_title, text=input_text, date_added=current_date)
    return HttpResponseRedirect(reverse('home:index'))


def deleteTodo(request, todo_id):
    my_todo = Todo.objects.get(pk=todo_id)
    my_todo.delete()
    return HttpResponseRedirect(reverse('home:index'))