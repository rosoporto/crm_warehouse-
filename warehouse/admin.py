from django.contrib import admin
from .models import Category, Supplier, Product, Inventory, Order, Client, OrderItem
from .forms import OrderItemForm


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'price', 'article', 'category')
    search_fields = ('name', 'category__name')

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    form = OrderItemForm  # Используем кастомную форму
    extra = 1  # Количество пустых форм для добавления новых позиций


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'tracking_number', 'created_at')  # Добавляем tracking_number в список отображаемых полей
    search_fields = ('client__name',)
    inlines = [OrderItemInline]


admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Inventory)
admin.site.register(Client)
