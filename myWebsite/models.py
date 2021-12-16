from django.db import models

# Create your models here.

class tb_news(models.Model):
    toppic_news = models.CharField(max_length=100)
    detail_news = models.TextField()
    photo_news = models.ImageField(upload_to = 'photo', default='')
    date_news = models.DateTimeField(auto_now=True, blank=False)
    