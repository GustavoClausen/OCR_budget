from django.urls import path

from .views import budget_form, delete_budget

urlpatterns = [
    path('', budget_form, name='budget_form'),
    path('delete/<uuid:pk>/', delete_budget, name='delete_budget'),
]
