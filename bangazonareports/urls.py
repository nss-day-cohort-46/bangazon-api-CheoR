"""Urls for Bangazon Report app"""

from django.urls import path
from .views import inexpensive_products_list, expensive_products_list

urlpatterns = [
    path('reports/inexpensiveproducts', inexpensive_products_list),
    path('reports/expensiveproducts', expensive_products_list),
]
