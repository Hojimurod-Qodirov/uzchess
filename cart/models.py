from django.db import models
from user.models import CustomUser

class PurchasedItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=50)  # Курс, книга, и т.д.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.item_name} ({self.item_type})"