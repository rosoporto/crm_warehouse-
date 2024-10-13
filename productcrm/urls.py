from django.contrib import admin
from django.urls import path, include
from productcrm import views


urlpatterns = [
    path('', views.index_page, name='main'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('warehouse/', include('warehouse.urls')),
    path('admin/', admin.site.urls),
]


handler404 = views.page_not_found
handler500 = views.server_error
