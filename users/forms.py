from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

"""
It inherits from the UserCreationForm form.
"""


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    """
    This class is a nested namespace for configuration (it keeps them in one place). 
    model: Specify the model that this form is going to interact with.
    fields: Specify the fields that will be shown on the form.
    'password1' is the first password field, while 'password2' is the password confirmation field.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
