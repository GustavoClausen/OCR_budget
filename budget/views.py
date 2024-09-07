from django.shortcuts import render


def budget_form(request):
    return render(request, 'budget/form.html')


def get_budget(request):
    return render(request, 'budget/result.html')


def delete_budget(request):
    return None
