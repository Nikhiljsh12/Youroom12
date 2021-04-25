from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from web.models import MyPost

# Create your views here.

def home(request):
    items=MyPost.objects.all()
    context={"posts":items[::-1]}
    return render(request, 'web/home.html', context)

def upload(req):
    if req.method=="POST":
        pdf=req.POST.get('pdf')
        print(pdf)
        return HttpResponse("k")