from turtle import home
from xml.etree.ElementInclude import include
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.profile, name='home'),
    path('home/', views.home, name='home'),
    path('signup/', views.save, name='SignUp'),
    path('login/', views.signin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.logout, name='logout'),
    path('flights/', views.flights, name='flights'),
    path('reservation/', views.reservations, name='reservation'),
    path('admin1/', views.admin1, name='admin1')
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)