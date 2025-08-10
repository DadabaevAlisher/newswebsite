from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
     

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    catogory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, related_name='news')
    title =models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    