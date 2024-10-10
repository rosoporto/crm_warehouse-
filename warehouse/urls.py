from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wrhs_index_page, name='warehouse_main'),
    path('categories/<int:cat_id>/', views.wrhs_get_categories_id, name='cagegory_id'),

]
