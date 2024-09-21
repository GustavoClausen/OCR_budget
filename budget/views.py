from django.shortcuts import render

from .form import BudgetForm


def budget_form(request):

    if request.POST:
        print(request.POST)
        form = BudgetForm(request.POST, request.FILES)
    else:
        form = BudgetForm()
    return render(request, 'budget/form.html', context={
        'form': form,
    })


def get_budget(request):
    return None


def delete_budget(request):
    return None
