from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    parent = models.ForeignKey('self', related_name='subtasks', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField()

    def __unicode__(self):
        return self.name
