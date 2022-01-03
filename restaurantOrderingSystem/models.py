from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import CASCADE


class OrderStatus(models.TextChoices):
    PENDING = 'PE', _('انتظار التجهيز')
    PREPARING = 'PR', _('تجهيز')
    WAITING = 'WA', _('بانتظار التسليم')
    DONE = 'DO', _('تم التسليم')


class Customer(models.Model):
    tableno = models.CharField(max_length=255)
    table_status = models.CharField(max_length=2, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tableno


class Qrcode(models.Model):
    qr_image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Order(models.Model):
    table_number = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    total = models.FloatField()
    customer = models.ForeignKey(Customer, related_name='ordering', on_delete=CASCADE)
    order_status = models.CharField(max_length=2, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    foodlist = models.ManyToManyField('Meal', related_name='order')

    def __str__(self):
        return 'order number is {} and total is {}'.format(self.table_number, self.total)


class Category(models.Model):
    meal_type = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal_type


class Meal(models.Model):
    meal_name = models.CharField(max_length=225)
    price = models.FloatField()
    description = models.CharField(max_length=225)
    meal_image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name="category_meals", on_delete=CASCADE)
    orderlist = models.ManyToManyField(Order, related_name='order', null=True, blank=True)

    def __str__(self):
        return self.meal_name


class Food_Pick(models.Model):
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='my_food', on_delete=CASCADE)
    meal = models.ForeignKey(Meal, related_name="food", on_delete=CASCADE)

    def __str__(self):
        return str(self.quantity)
