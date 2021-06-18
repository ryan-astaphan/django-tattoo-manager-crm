from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Artist, Booking
from .forms import AddArtistForm, AddTattooShopForm, AddBookingForm

# Dashboard View
class DashboardView(TemplateView):
    template_name = 'dashboard/_dashboard.html'


# Tattoo Shop Views
class AddTattooShopView(CreateView):
    template_name = 'dashboard/tattooshop_add.html'
    form_class = AddTattooShopForm


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
    template_name = 'dashboard/artist_add.html'
    form_class = AddArtistForm


class ArtistListView(ListView):
    model = Artist
    context_object_name = 'Artists'
    template_name = 'dashboard/artists.html'


# Booking Views
class BookingListView(ListView):
    model = Booking
    context_object_name = 'Bookings'
    template_name = 'dashboard/bookings.html'
    

class AddBookingView(CreateView):
    template_name = 'dashboard/booking_add.html'
    form_class = AddBookingForm