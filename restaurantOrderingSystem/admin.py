from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Meal)
admin.site.register(models.Order)
admin.site.register(models.Qrcode)
# admin.site.register(models.Invoice)
admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Food_Pick)