from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Burger, Basket


def burgers(request):
    context = {
        'title': 'Burgers',
        'burgers': Burger.objects.all()
    }
    return render(
        request,
        'burgers/burgers.html',
        context
    )


def data_user(request):
    context = {
        'title': 'Оформление заказа',
    }
    return render(
        request,
        'burgers/profile.html',
        context
    )


def basket_add(request, burger_id):
    burger = Burger.objects.get(id=burger_id)
    baskets = Basket.objects.filter(user=request.user, burgers=burger)

    if not baskets.exists():
        Basket.objects.create(user=request.user, burgers=burger, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


