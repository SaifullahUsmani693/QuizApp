from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms.widgets import *


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(
            choices=choice_list, widget=RadioSelect)


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded-pill form-control-lg',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded-pill form-control-lg',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill form-control-lg',
                    'placeholder': 'First Name',
                }
            ),



            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill form-control-lg',
                    'placeholder': 'Last Name',
                }
            ),

            'username': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill form-control-lg',
                    'placeholder': 'Username',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control rounded-pill form-control-lg',
                    'placeholder': 'Email',
                }
            ),


        }
