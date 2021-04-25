from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class MyPost(models.Model):
    head=models.CharField(default="Unknown",max_length=32)
    doc_by= models.ForeignKey(to=User, on_delete=CASCADE)
    doc=models.FileField(upload_to = "images\\")
    cr_date=models.DateTimeField(auto_now_add=True)
    background=models.CharField(max_length=20, default="", choices=(("#0a4b94","Blu"),("#DAA520","Yel"),("#95001b","Red"),("#463f85","Pur"),("#009342","Gre"),("#930051","Pin"),("","Non")))

class MyPage(models.Model):
    text=models.TextField()
    post=models.ForeignKey(to=MyPost, on_delete=CASCADE)
    page=models.IntegerField()
