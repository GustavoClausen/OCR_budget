from django.shortcuts import render
from django.shortcuts import HttpResponse

from .forms import BudgetForm


def budget_form(request):

    if request.method == 'POST':
        form = BudgetForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse(
                'Fazer o processamento dos arquivos e salvar na base de dados'
            )
    else:
        form = BudgetForm()

    return render(request, 'budget/form.html', context={
        'form': form,
    })


def delete_budget(request):
    return None
