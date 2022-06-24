from django import forms
from .models import OsauhinguAndmedModel


class OsauhinguAndmedForm(forms.ModelForm):
    class Meta:
        model = OsauhinguAndmedModel
        fields = "__all__"
