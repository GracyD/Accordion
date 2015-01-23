from django.db import models

# Create your models here.

class Article(models.Model):
	article_title = models.CharField(max_length=200)
	article_body = models.CharField(max_length=2000)
	article_pub_date = models.DateTimeField('date published')