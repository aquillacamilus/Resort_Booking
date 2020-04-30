from django.shortcuts import render

# Create your views here.
def welcome(req):
    return render(req,'mainapp/welcome.html')

def home(req):
    return render(req,'mainapp/Home.html')

def signup(req):
    return render(req,'mainapp/signup.html')

def login(req):
    return render(req,'mainapp/login.html')
