from django.contrib.auth.models import User
from django.db import models

# Create your models here.

type_choices = [('feature', 'feature'),
                ('bug', 'bug')]


status_choices = [('created', 'created'),
                  ('on_going', 'on_going'),
                  ('rejected', 'rejected'),
                  ('completed', 'completed')]


priority_choices = [('low', 'low'),
                    ('normal', 'normal'),
                    ('high', 'high'),]


class Project(models.Model):
    title = models.CharField(max_length=256)


class Tag(models.Model):
    name = models.CharField(max_length=256)


class Epic(models.Model):
    name = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='epic')


class Task(models.Model):
    title = models.CharField(max_length=256)
    type = models.CharField(max_length=7, choices=type_choices)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=9, choices=status_choices)
    priority = models.CharField(max_length=6, choices=priority_choices)
    description = models.TextField(max_length=256)
    owners = models.ManyToManyField(User)
    linked_tasks = models.ManyToManyField('user_tasks.Task')
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_tasks')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')


class TaskChange(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='changes')
    old_version = models.TextField()
    new_version = models.TextField()
    time_change = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_changes')
