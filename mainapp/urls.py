from django.conf.urls import url
from django.urls import path
from mainapp import views

#template tagging
app_name = 'mainapp'
urlpatterns=[
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.ulogin,name='login'),
    path('details/<int:pk>/',views.details,name='details'),
    path('reservation/<int:pk>/',views.reservation,name='reservation'),
    path('mybookings/',views.mybookings,name='mybookings'),
    path('delete/<int:pk>/', views.dele, name='delPage'),
    path('update/<int:pk>/',views.update,name='update'),
]
