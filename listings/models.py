from django.db import models
from realtors.models import Realtor


# Create your models here.
class Listing(models.Model):
    emlakci = models.ForeignKey(Realtor, on_delete= models.DO_NOTHING) 
    # models.DO_NOTHING ifadesi realtor silinse de listing kaydı kalsın demek models.CASCADE ifadesi ise realtor silinirse ilişkili #listing kaydını da sil demek.
    baslik = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    ilce = models.CharField(max_length=200)
    il = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True)
    fiyat = models.IntegerField()
    yatak_odasi = models.IntegerField()
    tuvalet = models.DecimalField(max_digits=2, decimal_places=1)
    garaj = models.IntegerField(default=0)
    metre_kare = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    yayin_tarihi = models.DateField()

    def __str__(self):
        return self.baslik
    

    
