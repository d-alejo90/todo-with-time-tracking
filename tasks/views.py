from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.all()
    
    completed_count = tasks.filter(complete=True).count()
    incompleted_count = tasks.filter(complete=False).count()
    all_count = tasks.count()

    context = {
        'tasks': get_tasks_to_show(request, tasks),
        'completed_count': completed_count,
        'incompleted_count': incompleted_count,
        'all_count': all_count
    }
    return render(request, 'tasks/list.html', context)

def get_tasks_to_show(request, tasks): 
    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter') == 'complete':
            return tasks.filter(complete=True)
        if request.GET.get('filter') == 'incomplete':
            return tasks.filter(complete=False)
    return tasks

@login_required
def add_task(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.owner = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, "Task Created Successfully")
        return redirect('/')
    
    context = {
        'form': form,
        'title': 'Create Task'    
    }
    return render(request, 'tasks/task_form.html', context)

@login_required
def updateTask(request, id):
    task = get_object_or_404(Task, pk=id)
    #task = Task.objects.get(id=id)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Task Updated Successfully")
            return redirect('/')

    context = {
        'form': form,
        'title': 'Update Task',
        'task': task    
    }

    return render(request, 'tasks/task_form.html', context)

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        if task.owner != request.user and task.owner is not None:
            messages.add_message(request, messages.ERROR, "You can't delete this task because you are not the owner")
            return redirect('/')
        task.delete()
        messages.add_message(request, messages.SUCCESS, "Task deleted Successfully")
        return redirect('/')

    context = {'task': task}

    return render(request, 'tasks/delete_confirmation.html', context)
