from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.wrhs_index_page, name='warehouse_main'),
    path(
        'categories/<int:cat_id>/',
        views.wrhs_get_categories_id,
        name='cagegory_id'
    ),
    path('products/', views.wrhs_product_list, name='product_list'),
    path('product/<int:product_id>/', views.wrhs_get_product, name='product'),
    path('redirect/<int:cat_id>/', views.wrhs_redirect, name='redirect'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
