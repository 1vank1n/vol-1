from django.shortcuts import render, redirect, get_object_or_404
from pytodo.main.forms import TaskForm
from pytodo.main.models import Task


def home(request):
    return render(request, 'home.html', {'task_list': Task.objects.filter(parent=None)})


def new_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'new_task.html', {'form': form})


def del_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
