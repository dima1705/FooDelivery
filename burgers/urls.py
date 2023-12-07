from django.urls import path, include

from .views import burgers, basket_add, basket_remove

app_name = 'burgers'

urlpatterns = [
    path('', burgers, name='burgers'),
    path('baskets/add/<int:burger_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]