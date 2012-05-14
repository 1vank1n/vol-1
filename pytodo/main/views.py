from django.shortcuts import render, redirect, get_object_or_404
from pytodo.main.forms import TaskForm
from pytodo.main.models import Task


def home(request):
	task_list = Task.objects.filter(parent=None)
	form = TaskForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, 'home.html', locals())


def del_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
