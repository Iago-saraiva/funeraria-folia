from django.db import models

# Create your models here.
class Coffin(models.Model):
    model = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    size = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to='media/coffins')

class Order(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    death_description = models.TextField()
    body_weight = models.FloatField()
    coffin_estimated_size = models.FloatField()
    coffin = models.ForeignKey(Coffin, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    finished_order = models.BooleanField(default=False)