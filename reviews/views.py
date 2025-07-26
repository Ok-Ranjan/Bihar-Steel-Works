from django.shortcuts import render, redirect
from .models import CustomerReview
from .forms import ReviewForm

def testimonials(request):
    reviews = CustomerReview.objects.order_by('-created_at')[:10]  # latest 10 reviews
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')

    return render(request, 'reviews/testimonials.html', {
        'reviews': reviews,
        'form': form
    })
