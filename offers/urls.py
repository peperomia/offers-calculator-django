from django.urls import path
from . import views

urlpatterns = [
    # Products
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),

    # Services
    path("services/", views.service_list, name="service_list"),
    path("services/new/", views.service_create, name="service_create"),

    # RawMaterials
    path("rawMaterials/", views.rawMaterials_list, name = "rawMaterials_list"),
    path("rawMaterials/new", views.rawMaterials_create, name = "rawMaterials_create")
]
