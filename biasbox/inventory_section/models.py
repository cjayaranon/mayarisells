from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from location_field.models.plain import PlainLocationField

class Product_Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Location(models.Model):
    city_municipality = models.CharField(max_length=100)
    plain_location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.city_municipality


class Store(models.Model):
    '''
    Store also known as Warehouse
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Merch(models.Model):
    '''
    Merch also known as Product

    SKU = Stock Keeping Unit
    UPC = Universal Product Code
    '''
    id = models.AutoField(primary_key=True)
    #SKU
    product_code = models.CharField(max_length=100)
    #UPC
    barcode = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    product_description = models.CharField(max_length=2000)
    product_category = models.ForeignKey(
        Product_Category,
        on_delete=models.SET_NULL,
        null=True
        )
    
    def __str__(self):
        return f"{self.product_name} ({self.product_code})"


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    quantity_available = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator]
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE
        )
    merch = models.ForeignKey(
        Merch,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('store', 'merch')

    def __str__(self):
        return f"{self.merch.product_name} at {self.store.name}: {self.quantity_available} pcs"