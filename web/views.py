from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect,\
    JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from web.models import MyPost
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import urllib
from django.conf import settings
import PyPDF2
from pip._internal import req

# Create your views here.

class upload(CreateView):
    template_name= "web/home.html"
    model=MyPost
    fields=["head","doc","background"]
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.doc_by= self.request.user
        
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())
 
    def get_context_data(self, **kwargs):
        items=MyPost.objects.all()
        context={"posts":items[::-1]}
    
    
        
        
            
        return context
    
def doc(req):
    if req.POST:
        pk=req.POST.get('pk')
        page=int(req.POST.get('page'))
        pdf=MyPost.objects.get(pk=pk)
        
        pdfFileObject = open(pdf.doc.path,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        pageObject = pdfReader.getPage(page)
        text=pageObject.extractText()
        return JsonResponse({"data":text})
            

    
 