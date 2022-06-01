from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest
from usermanag.forms import CustomUserCreationForm, LoginForm, ChangeUser
from django.contrib.auth import get_user_model

user = get_user_model()

def dashboard(request):
    return render(request, "dashboard.html")

def register(request):

    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "dashboard.html")
        else:
            data = form.errors
            print(data)
            return render(request, "error.html", {'data' : data})

def error(request):
    return render(request, "error.html")

#, initial=request.user.first_name
#instance=request.user,


def profile(request):

    if request.method == "POST":
        form = ChangeUser(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
    form = ChangeUser()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['phone_number'].initial = request.user.phone_number
    form.fields['email'].initial = request.user.email
    data = {'form':form}
    return render(request, "profile.html", data)