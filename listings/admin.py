from django.contrib import admin
from .models import Listing
# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','baslik','is_published','fiyat','yayin_tarihi','emlakci')
    list_display_links = ('id', 'baslik',)
    list_filter = ('emlakci',)
    list_editable = ('is_published',)
    search_fields = ('baslik','adres','il','ilce','fiyat')
    #sayfa başına gösterilecek kayıt sayısı
    list_per_page = 25


