from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    article = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Client(models.Model):
    CLIENT_TYPE_CHOICES = (
        ('individual', 'Физическое лицо'),
        ('legal_entity', 'Юридическое лицо'),
        ('marketplace', 'Маркетплейс'),
    )

    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    channel = models.CharField(
        max_length=100,
        choices=(
            ('online', 'Онлайн'),
            ('in_store', 'В магазине'),
            ('other', 'Другое')
        ),
        default='online'
    )
    status = models.CharField(
        max_length=100,
        choices=(
            ('new', 'Новый'),
            ('on_assembly', 'На сборке'),
            ('delivery', 'Доставляется'),
            ('completed', 'Завершен'),
            ('canceled', 'Отменен')
        ),
        default='new'
    )
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'Заказ {self.id} - {self.product.name} для {self.client.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    minimum_quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Наличие'
        verbose_name_plural = 'Наличие'
