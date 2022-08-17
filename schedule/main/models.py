from django.db import models


class Task(models.Model):
    name_of_class = models.CharField(max_length=150, verbose_name='Дисциплина')
    teacher = models.CharField(max_length=100, verbose_name='Преподаватель')
    group = models.CharField(max_length=10, verbose_name='Группа')
    auditorium = models.IntegerField(verbose_name='Аудитория')
    type = models.CharField(max_length=50, verbose_name='Тип занятия')
    num_of_class = models.IntegerField(verbose_name='Номер занятия')
    date_of_class = models.DateField(verbose_name='Дата')
    description = models.TextField(blank=True, verbose_name='Описание')
