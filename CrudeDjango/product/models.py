from django.db import models




class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_detail=models.CharField(max_length=300)
    product_image=models.FileField(upload_to='images')


    def __str__(self):
        return self.product_name


