from django.shortcuts import render, redirect
from django.http import HttpResponse


def wrhs_index_page(request):
    return render(request, 'warehouse/index.html')


def wrhs_get_categories_id(request, cat_id):
    return HttpResponse(f'Категория ID: {cat_id}')


def wrhs_redirect(request, cat_id):
    redirect_map = {
        1: 'http://www.google.ru/',
        2: 'http://www.yandex.ru/',
        3: 'http://www.python.org/',
    }
    url = redirect_map.get(cat_id)
    if url:
        return redirect(url)
    return HttpResponse('Неизвестная категория')
