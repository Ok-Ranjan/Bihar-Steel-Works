from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('order/', views.order, name='order'),
    path('services/', views.services, name='services'),
    path('reviews/', views.reviews, name='reviews'),
    path('contact/', views.contact, name='contact'),
]