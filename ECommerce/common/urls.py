from django.urls import path
from . import views

app_name='common'

urlpatterns = [
    path ('cusotmer-signup/', views.c_signup, name='c-signup' ),
    path ('', views.home, name='homepage'),
    path ('customer-login/', views.c_login, name='c-login' ),
    path ('seller-login/', views.s_login, name='s-login' ),
    path ('seller-signup/', views.s_signup, name='s-signup' ),
]