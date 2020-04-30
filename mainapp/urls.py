from django.conf.urls import url
from django.urls import path
from mainapp import views

#template tagging
app_name = 'mainapp'
urlpatterns=[
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
]
