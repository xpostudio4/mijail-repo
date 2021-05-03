from django.contrib import admin

# Register your models here.
from user_tasks.models import Project


admin.site.register(Project)
