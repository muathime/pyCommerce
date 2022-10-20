from django.contrib import admin
from .models import Product, Offer

# Register your models here.
class ProdutAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')

admin.site.register(Product, ProdutAdmin)
admin.site.register(Offer, OfferAdmin)