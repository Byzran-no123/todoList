from django import forms
from .models import List,Client
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class FormList(forms.ModelForm):
    class Meta:
        model=List
        fields='__all__'
        
class FormClient(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class FormRegister(UserCreationForm):
    email=forms.EmailField(label="Email", required=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]