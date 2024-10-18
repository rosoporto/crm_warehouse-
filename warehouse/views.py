from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm, OrderForm


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


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # или другой URL
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Перенаправление на список заказов
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})