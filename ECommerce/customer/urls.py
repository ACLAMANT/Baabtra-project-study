from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path ('homepage/', views.c_home, name='homepage' ),]