from django.contrib import admin
from .models import TattooShop, Artist, Customer, Booking

# Register your models here.


admin.site.register(TattooShop)
admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(Booking)