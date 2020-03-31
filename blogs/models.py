from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	blog_body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	pic = models.ImageField(upload_to='images',blank=True)


	def __str__(self):
		return self.title

	def summary(self):
		return self.blog_body[:50] + ("....")

	class Meta:
		ordering = ['-timestamp',]








# Create your models here.
