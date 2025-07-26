from django import forms
from .models import CustomerReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ['name', 'rating', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }
