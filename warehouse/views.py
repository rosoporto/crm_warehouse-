from django.http import HttpResponse


def wrhs_index_page(request):
    return HttpResponse('<h1>Главная страница Warehouse App</h1>')


def wrhs_get_categories_id(request, cat_id):
    return HttpResponse(f'Категория ID: {cat_id}')
