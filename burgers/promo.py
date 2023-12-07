from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Burger, Basket, User

import random
import string


def get_promo_code(request):
    if request.method == 'POST':
        promo_code = request.POST['promo_code']
        user = request.user

        try:
            discount_user = User.objects.get(promo_code=promo_code)

            if discount_user == user:
                messages.error(request, 'Вы уже использовали этот промокод!')
            else:
                user.promo_code = promo_code
                user.save()
                messages.success(request, 'Промокод успешно использован!')
        except User.DoesNotExist:
            messages.error(request, 'Такого промокода не существует!')

        return redirect('burgers:index')

    context = {
        'title': 'Получение промокода',
    }
    return render(request, 'burgers/get_promo_code.html', context)


def generate_promo_code():
    promo_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print(promo_code)
    return promo_code


promo_code = generate_promo_code()

# Присвоение промокода пользователю
user.promo_code = promo_code
user.save()