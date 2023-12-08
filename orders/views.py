from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from django.contrib import messages
from burgers.models import Basket


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if not order.exists():
                OrderItem.objects.create(
                    order=order,
                    basket=basket
                )
            # очистка корзины
            basket.clear()
            messages.success(request, 'Спасибо, что доверяете нам. Ваш заказ обрабатывается.!')
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'basket': basket, 'form': form})