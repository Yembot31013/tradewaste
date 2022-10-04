from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(
                                   attrs={
                                     'placeholder': "Username",
                                     'class': 'form-control',
                                     'id': 'inputName'
                                   }
                               )
                               )
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(
                                   attrs={
                                       'placeholder': "Email Address",
                                       'class': 'form-control',
                                       'id': 'inputEmail'
                                   }
                             )
                             )
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': "Password",
                                        'class': 'form-control',
                                        'id': 'inputPassword'
                                    }
                                )
                                )
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': "Confirm Password",
                                        'class': 'form-control',
                                        'id': 'inputPassword'
                                    }
                                )
                                )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class OrderForm(forms.ModelsForm):
#     class Meta:
#         models = Payed_class
#         fields = ('country')
#         widgets = {'country': CountrySelectWidget()}