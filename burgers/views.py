from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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


@login_required
def basket_add(request, burger_id):
    burger = Burger.objects.get(id=burger_id)
    baskets = Basket.objects.filter(
        user=request.user,
        burgers=burger
    )

    if not baskets.exists():
        Basket.objects.create(
            user=request.user,
            burgers=burger,
            quantity=1
        )
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])