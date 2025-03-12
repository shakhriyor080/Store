from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Slide(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField('rasm')

    def __str__(self):
        return self.title
    




class Category1(models.Model):
    title = models.CharField('Category1', max_length=255, db_index=True)
    slug = models.SlugField('Manzil',unique=True)
   

    class Meta:
        verbose_name = "Category1"
        verbose_name_plural = "categor"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category1_detail_url', kwargs={'slug':self.slug})




class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=20000)
    slug = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.IntegerField(null=True)
    category1 = models.ForeignKey(Category1, on_delete=models.CASCADE, null=True, related_name='categor')

    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.description[:30] + '... read more'

    def shorten(self):
        return self.title[:10] + '...'
    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'slug':self.slug})