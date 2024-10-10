from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_page, name='main'),
    path('warehouse/', include('warehouse.urls')),
    path('admin/', admin.site.urls),
]
