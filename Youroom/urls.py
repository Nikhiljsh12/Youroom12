"""Youroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Youroom import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from allauth.account.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='web/')),
    path('web/', include('web.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
