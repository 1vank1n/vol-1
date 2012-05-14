from django.forms import ModelForm
from pytodo.main.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'text', 'parent']
