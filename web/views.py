from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    context={"hi":"hi"}
    return render(request, 'web/home.html', context)