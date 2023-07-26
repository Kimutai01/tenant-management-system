from django.db import models

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, default='default.jpg')
    photo_1 = models.ImageField(null=True, blank=True, default='default.jpg')
    photo_2 = models.ImageField(null=True, blank=True, default='default.jpg')
    # video = models.FileField(null=True, blank=True, default='default.mp4')
    bedrooms = models.IntegerField(null=True, blank=True)

    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
