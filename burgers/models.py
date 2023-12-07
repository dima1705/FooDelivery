from django.db import models
from users.models import User


class Burger(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='burgers')

    class Meta:
        verbose_name = 'Бургер'
        verbose_name_plural = 'Бургеры'

    def __str__(self):
        return f'{self.name} | {self.price}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    burgers = models.ForeignKey(to=Burger, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для: {self.user.username} | Продукт: {self.burgers.name}'

    def sum(self):
        return self.burgers.price * self.quantity


