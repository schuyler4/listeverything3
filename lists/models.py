from __future__ import unicode_literals

from django.db import models

# Create your models here.

class List(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	date = models.DateTimeField('date published')

	def __str__(self):
		return self.title
	

class List_Item(models.Model):
	content = models.CharField(max_length=200)
	the_list = models.ForeignKey(List, on_delete=models.CASCADE)

	def __str__(self):
		return self.content

