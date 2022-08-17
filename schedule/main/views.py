from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        tasks = Task.objects.all()

        if form.is_valid():

            my_date = form.cleaned_data['date']
            my_criterion = form.cleaned_data['cr_str']
            my_criterion_exists = my_criterion is not None
            date_filter = Task.objects.filter(date_of_class=my_date)
            title = form.cleaned_data['cr_str']

            if form.cleaned_data['criterion'] == 'prep':
                tasks = date_filter.filter(teacher=my_criterion).order_by('num_of_class')
                my_criterion_exists = my_criterion_exists and tasks.exists()

            elif form.cleaned_data['criterion'] == 'group':
                tasks = date_filter.filter(group=my_criterion).order_by('num_of_class')
                title = 'Группа '+title
                my_criterion_exists = my_criterion_exists and tasks.exists()

            elif form.cleaned_data['criterion'] == 'audit':
                tasks = date_filter.filter(auditorium=my_criterion).order_by('num_of_class')
                title = 'Аудитория '+title
                my_criterion_exists = my_criterion_exists and tasks.exists()

            else:
                form = TaskForm()

            if not my_criterion_exists:
                return render(request, "main/index.html", {'title': title, 'empty_text': 'Ничего не найдено :(', 'form': form})
            else:
                return render(request, "main/index.html", {'title': 'Расписание', 'tasks': tasks, 'form': form})

    else:
        form = TaskForm()
        return render(request, "main/index.html", {'title': 'Расписание', 'empty_text': '',  'form': form})
