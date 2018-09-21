from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class MovieReview(models.Model):
	movie_name		= models.CharField(max_length=120)
	genre			= models.CharField(max_length=120, null=True, blank=True)
	director		= models.CharField(max_length=120, null=True, blank=True)
	release_date	= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	slug			= models.SlugField(null=True, blank=True)
	def  __str__(self):
		return self.movie_name

	@property
	def title(self):
		return self.movie_name

def pre_save_reciever(sender, instance, *args, **kwargs):
	# print('saving')
	# print(instance.release_date)
	if not instance.slug:
		instance.slug  = unique_slug_generator(instance)

# def post_save_reciever(sender, instance, created, *args, **kwargs):
# 	print('saved')
# 	print(instance.release_date)
# 	if not instance.slug:
# 		instance.slug  = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=MovieReview)
# post_save.connect(post_save_reciever, sender=MovieReview)
