from django.db import models
from django.core.validators import RegexValidator

class Pizzeria(models.Model):
	pizzeria_name = models.CharField(max_length=200, blank=False)
	street = models.CharField(max_length=400, blank=True)
	city = models.CharField(max_length=400, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True)
	zip_code = models.IntegerField(blank=True, default=0)
	website = models.URLField(max_length=420, blank=True)
	phone_number = models.CharField(validators=[RegexValidator(regex=r'^\d{9,10}$')], max_length=10, blank=True)
	description = models.TextField(blank=True)
	logo_image =  models.ImageField(upload_to='pizzariaImages', blank=True, default="pizzariaImages/pizzalogo.png")
	email = models.EmailField(max_length=254, blank=True)
	active = models.BooleanField(default=True)
	
	def __str__(self):

		return "{}, {}".format(self.pizzeria_name, self.city)

class Image(models.Model):
	pizzeria = models.ForeignKey(Pizzeria, on_delete=models.CASCADE, related_name='pizzeria_images',blank=True, null=True)
	image = models.ImageField(upload_to='photos',blank=True)
	image_title = models.CharField(max_length=120, blank=True)
	uploded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-uploded_at']