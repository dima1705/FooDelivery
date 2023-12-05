from django.shortcuts import render
from .models import Burger


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
