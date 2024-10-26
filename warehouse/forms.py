from django import forms
from .models import Product, Inventory, Order, Client, OrderItem
from django.forms import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'article',
                  'price',                  
                  'image',
                  'is_active',
                  'category',
                  'supplier'
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']  # Добавляем новое поле

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        inventory = super().save(commit=False)
        if commit:
            inventory.save()
        return inventory

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError('Количество не может быть отрицательным')
        return quantity

    def clean_minimum_quantity(self):
        minimum_quantity = self.cleaned_data['minimum_quantity']
        if minimum_quantity < 0:
            raise forms.ValidationError('Минимальное количество не может быть отрицательным')
        return minimum_quantity


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
    
    def save(self, commit=True):
        client = super().save(commit=False)
        if commit:
            client.save()
        return client


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['channel', 'status', 'comments', 'client']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        
    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        # Получаем все продукты, которые есть на складе
        available_products = Inventory.objects.filter(quantity__gt=0).values_list('product', flat=True)
        self.fields['product'].queryset = Product.objects.filter(id__in=available_products)


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm, extra=1, can_delete=True
)
