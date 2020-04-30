from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>second line</em>")
# Create your views here.
