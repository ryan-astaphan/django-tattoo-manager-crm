from django.contrib import admin
from .models import TattooShop, Artist, Customer, Transactions

# Register your models here.
class TattooShopAdmin(admin.ModelAdmin):
    pass
    # forms 
    # list_display = ['shop_name',]


class ArtistAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(TattooShopAdmin, ArtistAdmin, CustomerAdmin, TransactionAdmin)