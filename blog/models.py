from django.db import models


class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=500)
	body = models.TextField()
	published_date = models.DateTimeField()
