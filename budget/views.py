from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import HttpResponse

from .form import BudgetForm


def budget_form(request):
    previous_data = request.session.get('form_data', None)
    form = BudgetForm(previous_data)

    return render(request, 'budget/form.html', context={
        'form': form,
    })


def get_budget(request):
    if not request.POST:
        raise Http404()

    filled_data = request.POST
    filled_files = request.FILES

    request.session['form_data'] = filled_data

    form = BudgetForm(filled_data, filled_files)

    if not form.is_valid():
        return redirect('budget_form')

    del request.session['form_data']

    return HttpResponse('Fazer o processamento dos arquivos e salvar na base de dados')


def delete_budget(request):
    return None
