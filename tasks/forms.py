from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete'];
        
    input_attrs = {'class': 'block border border-grey-light w-full p-3 rounded mb-4'}
    
    title = forms.CharField(widget=forms.TextInput(attrs=input_attrs))
    description = forms.CharField(widget=forms.Textarea(attrs=input_attrs))
    complete = forms.BooleanField(
        initial=False,
        required=False,
        label='Is Completed?',
        widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-green-700'})
    )