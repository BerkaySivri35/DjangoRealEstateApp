from django.db import models

# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField(blank=True)
    contact_date = models.DateField(auto_now=True, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name