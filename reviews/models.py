from django.db import models

class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, f'{i} Stars') for i in range(1, 6)])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}★"
