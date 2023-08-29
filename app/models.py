from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField('店舗名', max_length=100)
    address = models.CharField('住所', max_length=100, null=True, blank=True)
    tel = models.CharField('番号',max_length=30, null=True, blank=True)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)

    def __str__(self):
        return self.name