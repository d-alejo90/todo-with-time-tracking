from django.shortcuts import render, redirect
from .models import Task
from .forms import *


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)


def updateTask(request, id):
    task = Task.objects.get(id=id)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}

    return render(request, 'tasks/delete_confirmation.html', context)
