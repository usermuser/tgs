from django.db import models

 class Catalog(models.Model):
 	name = models.CharField(max_length=255)
 	slug = models.SlugFiels(max_length=150)
 	description = model.TextField()

 class Product(models.Model):
 	name = models.CharField(max_length=300)
 	slug = models.SlugFiels(max_length=150)
 	description = models.TextField()
 	manufacturer = models.CharField(max_length=300, blank=True)
 	price = models.DecimalField(max_digits=6,decimal_places=2)


