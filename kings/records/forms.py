from django import forms
from .models import records


class Createrecord(forms.ModelForm):
    class Meta:
        model = records
        fields = ("kings", "times")
