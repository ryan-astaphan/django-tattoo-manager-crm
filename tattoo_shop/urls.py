from django.urls import path
from .views import (
    ArtistDetailView, 
    DashboardView, 
    ArtistListView, 
    AddTattooShopView,
    AddArtistView,
    AddBookingView,
    BookingListView,
    UpdateArtistView,
    )

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('add-tattoo-shop/', AddTattooShopView.as_view(), name='add_tattooshop'),
    path('add-artist/', AddArtistView.as_view(), name='add_artist'),
    path('artists/', ArtistListView.as_view(), name='artists'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('artists/<int:pk>/update/', UpdateArtistView.as_view(), name='artist_update'),
    path('bookings/', BookingListView.as_view(), name='bookings'),
    path('add-booking/', AddBookingView.as_view(), name='add_booking'),
]
