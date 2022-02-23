from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import events
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'
class eventsform(ModelForm):
    class Meta:
        model = events
        fields = ['eventname','link','lastdate','eventdate','time','location','slots','poster']
        widgets = {
            'eventdate': DateInput(),
            'lastdate': DateInput(),
            'time': forms.TimeInput(format='%H:%M'),
        }

