from django import forms

from .models import Artist, Booking, Customer, TattooShop


class AddTattooShopForm(forms.ModelForm):
    class Meta:
        model = TattooShop  
        fields = "__all__"
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


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