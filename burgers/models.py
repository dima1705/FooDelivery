from django.db import models


class Burger(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='burgers')

    def __str__(self):
        return f'{self.name} | {self.price}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


def random_number():
    import random
    rand = random.randrange(1000, 10001, 1)
    return rand


class Basket(models.Model):
    # uuid = models.SmallIntegerField(verbose_name='...', default=random_number)
    burgers = models.ForeignKey(to=Burger, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина: {self.user.username} | Продукт: {self.product.name}'


