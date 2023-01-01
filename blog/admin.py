from django.contrib import admin
from .models import  *
# Register your models here.

class AdminArtikel(admin.ModelAdmin):
    list_display = ["penulis","judul", "konten", "date", "picture"]

admin.site.register(Artikels, AdminArtikel)

class AdminProv(admin.ModelAdmin):
    list_display = ["id_prov", "prov"]

admin.site.register(ProvAPI, AdminProv)

class AdminKab(admin.ModelAdmin):
    list_display = ["id_kota", "kota"]

admin.site.register(KotaAPI, AdminKab)