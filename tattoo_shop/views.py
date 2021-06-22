from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Artist, Booking, TattooShop, Customer
from .forms import (
    AddArtistForm, 
    AddTattooShopForm, 
    AddBookingForm, 
    AddCustomerForm,
)

# Dashboard View
class DashboardView(TemplateView):
    template_name = 'dashboard/_dashboard.html'


# Tattoo Shop Views
class AddTattooShopView(CreateView):
    template_name = 'dashboard/tattooshop_add.html'
    form_class = AddTattooShopForm


class TattooShopListView(ListView):
    model = TattooShop
    context_object_name = 'Shops'
    template_name = 'dashboard/tattooshops.html'


class UpdateTattooShopView(UpdateView):
    model = TattooShop
    form_class = AddTattooShopForm
    template_name = 'dashboard/tattooshop_update.html'


class DeleteTattooShopView(DeleteView):
    model = TattooShop
    template_name = 'dashboard/tattooshop_delete.html'
    success_url = '/dashboard/tattoo-shops/'


# Artist Views
class AddArtistView(CreateView):
    template_name = 'dashboard/artist_add.html'
    form_class = AddArtistForm


class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'
    template_name = 'dashboard/artist_detail.html'


class UpdateArtistView(UpdateView):
    model = Artist
    form_class = AddArtistForm
    template_name = 'dashboard/artist_update.html'


class ArtistListView(ListView):
    model = Artist
    context_object_name = 'Artists'
    template_name = 'dashboard/artists.html'


class DeleteArtistView(DeleteView):
    model = Artist
    template_name = 'dashboard/artist_delete.html'
    success_url = '/dashboard/artists/'


# Booking Views
class BookingListView(ListView):
    model = Booking
    context_object_name = 'Bookings'
    template_name = 'dashboard/bookings.html'
    

class AddBookingView(CreateView):
    form_class = AddBookingForm
    template_name = 'dashboard/booking_add.html'


class BookingDetailView(DetailView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'dashboard/booking_detail.html'


class UpdateBookingView(UpdateView):
    model = Booking
    form_class = AddBookingForm
    template_name = 'dashboard/booking_update.html'


class DeleteBookingView(DeleteView):
    model = Booking
    template_name = 'dashboard/booking_delete.html'
    success_url = '/dashboard/bookings/'


# Customer Views
class AddCustomerView(CreateView):
    form_class = AddCustomerForm
    template_name = 'dashboard/customer_add.html'


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'Customers'
    template_name = 'dashboard/customers.html'


class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'dashboard/customer_detail.html'


class UpdateCustomerView(UpdateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'dashboard/customer_update.html'


class DeleteCustomerView(DeleteView):
    model = Customer
    template_name = 'dashboard/customer_delete.html'
    success_url = '/dashboard/customers/'