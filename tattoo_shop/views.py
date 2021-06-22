from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Artist, Booking, TattooShop, Customer
from .forms import (
    AddArtistForm, 
    AddTattooShopForm, 
    AddBookingForm, 
    AddCustomerForm,
)

# Dashboard View
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/_dashboard.html'


# Tattoo Shop Views
class AddTattooShopView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/tattooshop_add.html'
    form_class = AddTattooShopForm
    

class TattooShopListView(LoginRequiredMixin, ListView):
    model = TattooShop
    context_object_name = 'shops'
    template_name = 'dashboard/tattooshops.html'


class UpdateTattooShopView(LoginRequiredMixin, UpdateView):
    model = TattooShop
    form_class = AddTattooShopForm
    template_name = 'dashboard/tattooshop_update.html'


class DeleteTattooShopView(LoginRequiredMixin, DeleteView):
    model = TattooShop
    template_name = 'dashboard/tattooshop_delete.html'
    success_url = '/dashboard/tattoo-shops/'


# Artist Views
class AddArtistView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/artist_add.html'
    form_class = AddArtistForm


class ArtistDetailView(LoginRequiredMixin, DetailView):
    model = Artist
    context_object_name = 'artist'
    template_name = 'dashboard/artist_detail.html'


class UpdateArtistView(LoginRequiredMixin, UpdateView):
    model = Artist
    form_class = AddArtistForm
    template_name = 'dashboard/artist_update.html'


class ArtistListView(LoginRequiredMixin, ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'dashboard/artists.html'

    def get_queryset(self):
        return Artist.objects.filter(tattoo_shop__user=self.request.user)


class DeleteArtistView(LoginRequiredMixin, DeleteView):
    model = Artist
    template_name = 'dashboard/artist_delete.html'
    success_url = '/dashboard/artists/'


# Booking Views
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    context_object_name = 'bookings'
    template_name = 'dashboard/bookings.html'
    

class AddBookingView(LoginRequiredMixin, CreateView):
    form_class = AddBookingForm
    template_name = 'dashboard/booking_add.html'


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'dashboard/booking_detail.html'


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = AddBookingForm
    template_name = 'dashboard/booking_update.html'


class DeleteBookingView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'dashboard/booking_delete.html'
    success_url = '/dashboard/bookings/'


# Customer Views
class AddCustomerView(LoginRequiredMixin, CreateView):
    form_class = AddCustomerForm
    template_name = 'dashboard/customer_add.html'


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'dashboard/customers.html'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'dashboard/customer_detail.html'


class UpdateCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'dashboard/customer_update.html'


class DeleteCustomerView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'dashboard/customer_delete.html'
    success_url = '/dashboard/customers/'