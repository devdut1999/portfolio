from django.db import models


class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=500)
	body = models.TextField()
	published_date = models.DateTimeField()

	def  __str__(self):
		return self.title

	def summary(self):
		return self.body[:90]

	def pub_date_pretty(self):
		return self.published_date.strftime('%b %e %Y')	