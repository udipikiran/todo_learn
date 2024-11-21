from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    complted_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'completed_tasks':complted_tasks,
    }
    print(tasks)
    return render(request, 'home.html', context)