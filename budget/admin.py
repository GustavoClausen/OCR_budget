from django.contrib import admin

from .models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'whatsapp_number',
        'source_language',
        'target_language'
    )
