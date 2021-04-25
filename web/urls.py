from django.contrib import admin
from django.urls import path
from web import views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView
from django.urls.conf import include

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.home),
]
