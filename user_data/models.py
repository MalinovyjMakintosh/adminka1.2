from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    replenishment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    withdrawal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    community_count = models.PositiveIntegerField(default=0)
    creative_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username