from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# https://github.com/stefanfoulis/django-phonenumber-field
# pipenv install django-phonenumber-field[phonenumbers]
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class TattooShop(models.Model):
    shop_name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.shop_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.shop_name)


class Artist(models.Model):
    tattoo_shop = models.ForeignKey(TattooShop, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=30)
    commission = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ], 
        verbose_name='Commission %',
        help_text='Enter a number from 0-100'
    )
    is_manager = models.BooleanField(
        null=True,
        help_text='Check this box to give manager permissions.'
        )
    
    def __str__(self):
        return self.artist_name


class Customer(models.Model):
    tattoo_shop = models.ForeignKey(TattooShop, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30, default='Guest')
    # Need to install phonenumber package for the PhoneNumberField
    # customer_phone_number = PhoneNumberField(null=True, blank=True)
    customer_email = models.EmailField(max_length=50, null=True, blank=True)
    customer_facebook_name = models.CharField(max_length=30, null=True, blank=True)
    customer_instagram = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.customer_name


class Transactions(models.Model):
    tattoo_shop = models.ForeignKey(
        TattooShop, 
        on_delete=models.CASCADE, 
        # editable=False (I'm not sure if this is correct) 
        )
    customer = models.ForeignKey(Customer, null=TRUE, on_delete=models.SET_NULL)
    artist = models.ForeignKey(artist, on_delete=models.SET_NULL)
    appointment_date = models.DateField()
    tattoo_description = models.TextField(max_length=300)
    custom_design = models.BooleanField(help_text='Check the box if the \
        customer needs a custom design',
        null=True)
    custom_design_finished = models.BooleanField(help_text='Check the box \
        if the design is finalized',
        null=True)
    deposit_amount = models.DecimalField(min_value=0.0, 
    decimal_places=2,
    help_text='Enter only if a customer paid a deposit',
    default=0.0)
    deposit_date = models.DateField(blank=True,
    null=True,)
    quote = models.CharFieldField(
        max_length=30,
        help_text='If you gave a quoted price, enter it here to remember',
        blank=True)
    final_payment = models.DecimalField(min_value=0.0, decimal_places=2)
    artist_paid = models.BooleanField(
        default=False,
        help_text="Check here after you've paid your artist"
    )

    