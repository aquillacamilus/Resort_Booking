from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
# Create your views here.
def welcome(req):
    return render(req,'mainapp/welcome.html')

@login_required
def home(req):
    return render(req,'mainapp/Home.html')

def signup(req):
    if req.method == 'POST':
        user_form = UserForm(data=req.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            return HttpResponseRedirect(reverse('mainapp:login'))
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
    return render(req,'mainapp/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('welcome'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request,'Incorrect username or password')
            return redirect('mainapp:login')
    return render(request,'mainapp/login.html')
