from django import forms

from .models import Artist, Booking, Customer, TattooShop


class AddTattooShopForm(forms.ModelForm):
    class Meta:
        model = TattooShop  
        fields = "__all__"


class AddArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'tattoo_shop',
            'artist_name',
            'commission',
            'is_manager'
        ]


class AddBookingForm(forms.ModelForm):
    class Meta:
        model = Booking  
        fields = "__all__"


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"