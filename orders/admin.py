from django import forms
from django.contrib import admin
from orders.models import Order


class OrderAdminForm(forms.ModelForm):
    class Meta(object):
        model = Order
        fields = '__all__'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('order_sum', 'status', 'approved_at', 'created_at', 'updated_at')
    list_filter = ('status', )

