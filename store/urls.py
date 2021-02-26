from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:product_id>/product/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]