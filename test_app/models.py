from django.db import models

class Post(models.Model):
	caption_text = models.TextField()
	pub_date = models.DateTimeField() 

# Create your models here.
