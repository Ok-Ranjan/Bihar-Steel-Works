from django.shortcuts import render
from reviews.models import CustomerReview

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def products(request):
    return render(request, 'website/products.html')

def order(request):
    return render(request, 'website/order.html')

def services(request):
    return render(request, 'website/services.html')

def reviews(request):
    reviews = CustomerReview.objects.order_by('-created_at')[:6]  # latest 6 reviews
    return render(request, 'website/reviews.html', {'reviews': reviews})

def contact(request):
    return render(request, 'website/contact.html')