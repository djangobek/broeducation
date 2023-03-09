from django import forms
from django.forms import ModelForm
from .models import MyfutureForm
class BlogForm(ModelForm):
    class Meta:
        model = MyfutureForm
        fields = ('full_name','phone_number','description')
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control item'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control item'}),
            'description':forms.TextInput(attrs={'class':'form-control item'}),
        }

