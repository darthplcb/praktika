from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name_of_class', 'teacher', 'group', 'auditorium', 'type', 'num_of_class', 'date_of_class')
    search_fields = ('teacher', 'group', 'auditorium', 'date_of_class')


admin.site.register(Task, TaskAdmin)
