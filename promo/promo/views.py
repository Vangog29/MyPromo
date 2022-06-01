from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def index(response):
    return render(response, "index.html")
