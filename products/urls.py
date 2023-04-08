from django.urls import path

from .views import *

urlpatterns = [
    path("all", list_products)
]