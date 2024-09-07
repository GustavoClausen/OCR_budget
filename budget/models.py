import uuid
from django.db import models


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=250, null=False)
    email = models.EmailField(null=False)
    whatsapp_number = models.CharField(max_length=100, null=False)
    source_language = models.CharField(max_length=100, null=False)
    target_language = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)
    total_words = models.IntegerField(null=False)
    created_at = models.DateField(auto_now_add=True)


class File(models.Model):
    budget = models.ForeignKey(
        to=Budget,
        on_delete=models.CASCADE,
    )
    file = models.FileField(null=False)
