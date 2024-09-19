from django.shortcuts import render
from django.http import Http404


def budget_form(request):
    return render(request, 'budget/form.html')


def get_budget(request):
    if not request.POST:
        return Http404()

    print(request.POST)

    return render(request, 'budget/result.html')


def delete_budget(request):
    return None
