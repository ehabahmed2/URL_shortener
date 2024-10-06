from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Login

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegisterUser, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.ModelForm):
    class Meta: 
        model = Login
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
