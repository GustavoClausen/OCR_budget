from django.db import models


class Budget(models.Model):
    full_name = models.CharField(max_length=250, null=False)
    email = models.EmailField(null=False)
    whatsapp_number = models.CharField(max_length=100, null=False)
    source_language = models.CharField(max_length=100, null=False)
    target_language = models.CharField(max_length=100, null=False)


class File(models.Model):
    budget = models.ForeignKey(
        to=Budget,
        on_delete=models.CASCADE,
    )
    file = models.FileField(null=False)
