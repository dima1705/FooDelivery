from django.shortcuts import render


def burgers(request):
    context = {
        'title': 'Burgers',
    }
    return render(
        request,
        'burgers/burgers.html',
        context
    )
