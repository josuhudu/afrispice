from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name' ,'password1', 'password2']

class RegisterForm(forms.Form):
    email = forms.EmailField(
    widget = forms.TextInput(
        attrs = {'name':'email','type':'email', 'class': 'form-control', 'placeholder':'Email'}
        )
    )

    first_name = forms.CharField(
    widget = forms.TextInput(
        attrs = {'name':'first_name','type':'text', 'class': 'form-control', 'placeholder':'First Name'}
        )
    )

    last_name = forms.CharField(
    widget = forms.TextInput(
        attrs = {'name':'last_name','type':'text', 'class': 'form-control', 'placeholder':'Last Name'}
        )
    )

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(
                attrs={'required':'','name':'email', 'maxlength':'254', 'class':'emailinput form-control', 'id':'id_email', 'placeholder':'Email'}
                ),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']