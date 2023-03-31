from django import forms
from . import models

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['category', 'title', 'description']
        widgets = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = [ 'title','category', 'status']
        widgets = {
            'title': forms.TextInput(),
            'category': forms.Select(),
            'status': forms.Select()
        }
