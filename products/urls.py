from django.urls import path

from .views import *

urlpatterns = [
    path("create", createProduct),
    path("delete/<int:_id>", deleteProduct),
]