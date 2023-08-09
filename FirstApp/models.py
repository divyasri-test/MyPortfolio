from django.db import models
from datetime import datetime
# Create your models here.
# import the standard Django Model
# from built-in library



class DetailsModel(models.Model):

	# Field Names
	name = models.CharField(max_length=200)
	description = models.TextField()
	date_of_birth = models.DateTimeField(default=datetime.now)
	image = models.ImageField(upload_to="images/%Y/%m/%d")

	# rename the instances of the model
	# with their title name

