from django.http import HttpResponse


def index_page(request):
    return HttpResponse('<h1>Главная страница</h1>')