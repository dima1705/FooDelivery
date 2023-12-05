from django.db import models


class Burger(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='burgers')

    def __str__(self):
        return f'{self.name} | {self.price}'
