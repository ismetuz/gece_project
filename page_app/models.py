from django.db import models
from autoslug import AutoSlugField
from unidecode import unidecode
from django.db.models.signals import pre_save
from django.dispatch import receiver



def convert_to_slug(text):
    return unidecode(text)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    description = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='category_photo')



    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=Category)
def create_slug(sender, instance, **kwargs):
    instance.slug = convert_to_slug(instance.title)
    
class SliderItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    


class Products(models.Model):
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title', unique=True)  # Otomatik olarak slug oluşturur
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(Category)  # ForeignKey kullanıldı
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=Products)
def create_slug(sender, instance, **kwargs):
    instance.slug = convert_to_slug(instance.title)

class ContactInfo(models.Model):
    title = models.CharField(max_length=255)
    about_us = models.TextField()
    adress = models.TextField()
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField()
    iban=models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
