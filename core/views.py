from django.shortcuts import render
from .models import Dokon

# Create your views here.
def index(request):
    
    dokonlar = Dokon.objects.all()
    dokon_list = []
    
    for dokon in dokonlar:
        mahsulotlar = dokon.mahsulotlar.all()
        dokon_list.append(
            {
                "dokon" : dokon,
                "mahsulotlar": mahsulotlar
            }
        )
    
    
    return render(request,"core/index.html",{"dokon_list": dokon_list})