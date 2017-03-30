from django.db import models

# Create your models here.
class UsersAccount(models.Model):

	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	
	# email= models.CharField(max_length=20)
	# gender=models.CharField(max_length=20)
	# firstLocation=models.CharField(max_length=20)
	# username = models.CharField(max_length=20)
	# password = models.CharField(max_length=20)