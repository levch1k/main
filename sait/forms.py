from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Statement


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'fio', 'phone', 'email', 'password1', 'password2']
        labels = {
            'fio': 'Введите ФИО:',
            'phone': 'Введите номер телефона:',
            'email': 'Введите адресс:',
        }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CreateStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['imposter', 'describe']
        # widgets = {
        #     'imposter': forms.TextInput(attrs=)
        # }
        labels = {
            'imposter': 'Введите ФИО нарушителя',
            'describe': 'Опишите нарушение',
        }