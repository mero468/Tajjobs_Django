from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Terms', views.terms, name='Terms'),
    path('Privacy', views.privacy, name='Privacy'),
    path('Login', views.login, name='Login'),
    path('Signup', views.signup, name='Signup')
]
