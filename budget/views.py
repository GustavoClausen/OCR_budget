from django.shortcuts import render
from django.http import Http404

from .form import BudgetForm


def budget_form(request):
    form = BudgetForm()

    return render(request, 'budget/form.html', context={
        'form': form,
    })


def get_budget(request):
    if not request.POST:
        return Http404()

    for file in request.FILES.getlist('files'):
        print(file)

    return render(request, 'budget/result.html')


def delete_budget(request):
    return None
