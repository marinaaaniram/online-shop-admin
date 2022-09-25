from django import forms
from django.contrib import admin
from products.models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta(object):
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'price', 'created_at', 'updated_at')