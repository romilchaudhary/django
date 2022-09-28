from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Products"