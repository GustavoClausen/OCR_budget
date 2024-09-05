from django.urls import path

from .views import budget_form, get_budget

urlpatterns = [
    path('', budget_form, name='budget_form'),
    path('get/', get_budget, name='get_budget'),
]
