from django.forms import ModelForm, DateInput
from . import models

class RequestForm(ModelForm):
    class Meta:
        model = models.Request
        fields = ('course', 'payment', 'prefered_start_date')