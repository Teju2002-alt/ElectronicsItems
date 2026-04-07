from django.db import models

# Create your models here.
class Electronics(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	brand = models.CharField(max_length=100)
	category = models.CharField(max_length=100)  
	rating = models.FloatField(null=True, blank=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True) 
	image = models.ImageField(upload_to='electronics/', null=True, blank=True)  

	def __str__(self):
		return self.name