from django.db import models

class People(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    age=models.IntegerField()
    image=models.FileField(upload_to='images')

    def __str__(self):
        return self.name

