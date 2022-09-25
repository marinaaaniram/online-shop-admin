from django import forms
from django.contrib import admin
from django.utils.html import format_html
from orders.models import Order
from payments.models import Payment


class OrderAdminForm(forms.ModelForm):
    class Meta(object):
        model = Order
        fields = '__all__'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('order_sum', 'get_order_status', 'get_payment_status', 'confirm_order_button', 'confirmed_at',
                    'created_at', 'updated_at',)
    list_filter = ('status', )

    def get_order_status(self, obj):
        return obj.status
    get_order_status.short_description = 'Order status'

    def get_payment_status(self, obj):
        return obj.payment.status
    get_payment_status.short_description = 'Payment status'

    def confirm_order_button(self, obj):
        if obj.payment.status == Payment.PAID and obj.status != Order.CONFIRMED:
            return format_html('<button class="button confirm_button" object_id="{}">Confirm</button>'.format(obj.id))
        elif obj.status == Order.CONFIRMED:
            return format_html('<text>✅</text>')
    confirm_order_button.short_description = 'Confirm order'
    confirm_order_button.allow_tags = True

    class Media:
        js = ('js/admin.js',)





