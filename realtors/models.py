from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    aciklama = models.TextField(blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    uyelik_tarihi = models.DateField()

    def __str__(self):
        return self.name