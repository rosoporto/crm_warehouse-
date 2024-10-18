from django import forms
from .models import Product, Inventory, Order, Client


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'article',
                  'price',
                  'quantity',
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
        fields = ['product', 'quantity', 'minimum_quantity']  # Добавляем новое поле

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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'product',
            'quantity',
            'channel',
            'status',
            'comments',
            'client'
        ]
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),  # Добавляем класс для стилизации
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all()  # Заполняем выбор клиентов

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order


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
