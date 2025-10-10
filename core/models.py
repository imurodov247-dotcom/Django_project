from django.db import models

# Create your models here.
class Dokon(models.Model):
    nomi = models.CharField(max_length=200)
    manzili = models.CharField()
    
    
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=200)
    narxi = models.FloatField()
    dokon = models.ForeignKey (Dokon, on_delete=models.CASCADE,related_name='mahsulotlar')
    
    