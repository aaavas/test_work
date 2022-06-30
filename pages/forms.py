from django import forms
from .models import OsanikModel, OsauhinguAndmedModel
from functools import partial


class OsauhinguAndmedForm(forms.ModelForm):
    class Meta:
        model = OsauhinguAndmedModel
        exclude = ("osanikud",)
