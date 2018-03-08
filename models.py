from django.db import models
from polymorphic.models import PolymorphicModel
from FOMO import settings

class Category(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(PolymorphicModel):

    TYPE_CHOICES = (
        ('BulkProduct','Bulk Product'),
        ('IndividualProduct','Individual Product'),
        ('RentalProduct','Rental Product'),
    )
    STATUS_CHOICES = (
        ('A','Active'),
        ('I','Inactive'),
    )
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField()
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7,decimal_places=2)

    def image_url(self):
        image = ProductImage.objects.filter(product = self)
        try:
            url = settings.STATIC_URL + 'catalog/media/products/' + image[0].filename
        except:
            url = settings.STATIC_URL + 'catalog/media/products/no_image.png'

        return url

    def image_urls(self):
        image = ProductImage.objects.filter(product = self)
        mylist=[]
        icount = 0

        #for each item in list
        try:
            for i1 in image:

                url = settings.STATIC_URL + 'catalog/media/products/' + i1.filename
                mylist.append([url])
                icount = icount+1
        except:
            url = settings.STATIC_URL + 'catalog/media/products/no_image.png'
            mylist.append([url])

        return mylist

    

class BulkProduct(Product):
    TITLE = 'Bulk'
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()

class IndividualProduct(Product):
    TITLE = 'Individual'
    pid = models.TextField()

class RentalProduct(Product):
    TITLE = 'Rental'
    pid = models.TextField()
    max_rental_days = models.IntegerField(default=0)
    retire_date = models.DateField(null=True,blank=True)

class ProductImage(models.Model):
    filename = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now =True)
    product = models.ForeignKey('Product', on_delete = models.CASCADE,related_name='images')



## empy NOT_FOUND_PRODUCT_IMAGE = ProductImage()
