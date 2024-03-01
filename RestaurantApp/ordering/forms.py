from .models import  AvailableItems
from django import forms

class EmpModelForm(forms.ModelForm):
    class Meta:
        model=AvailableItems
        fields='__all__'
