from django.shortcuts import render
from django.http import (
    HttpResponseNotFound,
    HttpResponseServerError
)


def index_page(request):
    context = {
        'title': 'Мой склад на Django',
        'content': 'Складская система учета товаров',
    }
    return render(request, 'index.html', context)


def about_page(request):
    context = {
        'title': 'О проекте',
        'content': 'Мой склад на Django: учёт товара',
    }
    return render(request, 'about.html', context)


def contact_page(request):
    context = {
        'title': 'Контакты',
        'email': 'example@example.com',
        'phone': '99999999999',
    }
    return render(request, 'contact.html', context)


def page_not_found(request, exception):
    HttpResponseNotFound('<h1>Page Not Found</h1>')


def server_error(request):
    HttpResponseServerError('<h1>Server Error</h1>')
