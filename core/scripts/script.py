from ..models import Dokon,Mahsulot

def run():
    dokon1 = Dokon.objects.create(nomi = "Anor market",manzili = "Yunusobod")
    dokon2 = Dokon.objects.create(nomi = "Grand  market",manzili = "Chilonzor")
    dokon3 = Dokon.objects.create(nomi = "Makro market",manzili = "Sergili")
    
    dokon1.mahsulotlar.create(nomi = "Olma", narxi = 16000)
    dokon1.mahsulotlar.create(nomi = "Banan", narxi = 15000)
    dokon1.mahsulotlar.create(nomi = "Uzum", narxi = 23000)
    
    
    dokon2.mahsulotlar.create(nomi = "Non", narxi =5000)
    dokon2.mahsulotlar.create(nomi = "Sut", narxi = 8000)
    dokon2.mahsulotlar.create(nomi = "Tuhum", narxi = 2000)
    
    dokon3.mahsulotlar.create(nomi = "Guruch", narxi = 16000)
    dokon3.mahsulotlar.create(nomi = "Yog'", narxi = 16000)
    dokon3.mahsulotlar.create(nomi = "Shakar", narxi = 16000)
    dokon3.mahsulotlar.create(nomi = "Tuz", narxi = 11000)
    
    