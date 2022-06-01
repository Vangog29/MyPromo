from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from usermanag.models import ExtendedUser
from django.forms import ModelForm 
from django.contrib.auth import get_user_model


from django.forms.models import model_to_dict
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
        model = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ChangeUser (ModelForm):


    first_name = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ExtendedUser
        fields = ["first_name", "last_name", "phone_number", "email"]
