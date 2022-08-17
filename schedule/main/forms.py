from django import forms
from .models import Task


class TaskForm(forms.Form):
    criterion = forms.ChoiceField(choices=(('prep', 'преподватель'), ('group', 'группа'), ('audit', 'аудитория')),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    cr_str = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'что ищем...'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
