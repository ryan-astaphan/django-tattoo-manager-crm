from django.urls import path
from .views import (
    DashboardView, 
    # TattooShop Views
    AddTattooShopView,
    TattooShopListView,
    UpdateTattooShopView,
    DeleteTattooShopView,
    # Artist Views
    AddArtistView,
    ArtistListView, 
    ArtistDetailView,  
    UpdateArtistView,
    DeleteArtistView,
    #Customer Views
    AddCustomerView,
    CustomerListView,    
    CustomerDetailView,
    UpdateCustomerView,
    DeleteCustomerView,
    # Booking Views
    AddBookingView,
    BookingListView,
    BookingDetailView,
    UpdateBookingView,
    DeleteBookingView,
    )

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('add-tattoo-shop/', AddTattooShopView.as_view(), name='add_tattooshop'),
    path('tattoo-shops/', TattooShopListView.as_view(), name='tattooshops'),
    path('<int:pk>/edit/', UpdateTattooShopView.as_view(), name='tattooshop_update'),
    path('<int:pk>/delete/', DeleteTattooShopView.as_view(), name='tattooshop_delete'),
    path('add-artist/', AddArtistView.as_view(), name='add_artist'),
    path('artists/', ArtistListView.as_view(), name='artists'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('artists/<int:pk>/edit/', UpdateArtistView.as_view(), name='artist_update'),
    path('artists/<int:pk>/delete/', DeleteArtistView.as_view(), name='artist_delete'),
    path('add-booking/', AddBookingView.as_view(), name='add_booking'),
    path('bookings/', BookingListView.as_view(), name='bookings'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('bookings/<int:pk>/edit/', UpdateBookingView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', DeleteBookingView.as_view(), name='booking_delete'),
    path('add-customer/', AddCustomerView.as_view(), name='add_customer'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit/', UpdateCustomerView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', DeleteCustomerView.as_view(), name='customer_delete'),
]
