from django.shortcuts import render,get_object_or_404
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from mainapp.models import Resorts,ReservationModel
from django.contrib import messages
# Create your views here.
def welcome(req):
    return render(req,'mainapp/welcome.html')

@login_required
def mybookings(req):
    x=ReservationModel.objects.all().filter(user=req.user)
    print(len(x))
    context={
        'objects':x
    }
    return render(req,'mainapp/mybookings.html',context)

@login_required
def dele(req,**kwargs):
    # print(kwargs['pk'])
    obj=get_object_or_404(ReservationModel,id=kwargs['pk'])
    if req.method == 'POST':
        obj.delete()
        messages.success(req, "Successfully Deleted")
    return HttpResponseRedirect(reverse('mainapp:mybookings'))

@login_required
def update(req,**kwargs):
    if req.method == 'POST':
        date=req.POST.get('date')
        adult=req.POST.get('adult')
        child=req.POST.get('child')
        obj2=get_object_or_404(ReservationModel,id=kwargs['pk'])
        obj2.bookDate=date
        obj2.adult=adult
        obj2.child=child
        obj2.total=int(adult)*(obj2.resortname.adult)+int(child)*(obj2.resortname.child)
        obj2.save()
        return HttpResponseRedirect(reverse('mainapp:mybookings'))
    x=get_object_or_404(ReservationModel,id=kwargs['pk'])
    c={
        'object':x,
        'date':str(x.bookDate),
        'lst':[0,1,2,3,4,5,6,7]
    }
    # obj=get_object_or_404(ReservationModel,id=kwargs['pk'])
    # c['date']=str(obj.bookDate)
    # c['adult']=obj.adult
    # c['pkk']=kwargs['pk']

    return render(req,'mainapp/update.html',c)

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('welcome'))

@login_required
def reservation(req,**kwargs):
    if req.method == 'POST':
        date=req.POST.get('date')
        adult=req.POST.get('adult')
        child=req.POST.get('child')
        id=kwargs['pk']
        obj=get_object_or_404(Resorts,id=kwargs['pk'])
        total=int(adult)*(obj.adult)+int(child)*(obj.child)
        print(adult,child,total)
        T=ReservationModel(user=req.user,bookDate=date,adult = adult,child = child,resortname = obj ,total = total)
        T.save()
        messages.success(req, "Successfully Booked")


    context={
        'object':get_object_or_404(Resorts,id=kwargs['pk'])
    }
    return render(req,'mainapp/reservation.html',context)

@login_required
def details(req,**kwargs):
    context={
        'object':get_object_or_404(Resorts,id=kwargs['pk'])
    }
    return render(req,'mainapp/resort1.html',context)

@login_required
def home(req):
    context={
        'objects':Resorts.objects.all()
    }
    return render(req,'mainapp/Home.html',context)

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

def ulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('mainapp:home'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request,'Incorrect username or password')
            return redirect('mainapp:login')
    return render(request,'mainapp/login.html')
