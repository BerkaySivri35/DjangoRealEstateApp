from django.contrib import admin

from .models import Realtor
# Register your models here.

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','uyelik_tarihi','is_mvp',)
    list_editable = ('is_mvp',)
    search_fields = ('name',)


