from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date','is_available')
    prepopulated_fields = {'slug': ('product_name',)}
      # Corregido 'modifield_date' a 'modified_date'

admin.site.register(Product, ProductAdmin)
