from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from web.models import MyPost

# Register your models here.

   
class MyPostAdmin(ModelAdmin):
    list_display=["pk","head","doc_by","doc","background","cr_date"]
    search_fields=["pk","head","doc","doc_by__username","cr_date"]
    list_filter=["doc_by","cr_date"]
    fields=[]
admin.site.register(MyPost, MyPostAdmin)
