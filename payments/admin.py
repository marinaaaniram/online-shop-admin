from django import forms
from django.contrib import admin
from payments.models import Payment


class PaymentAdminForm(forms.ModelForm):
    class Meta(object):
        model = Payment
        fields = '__all__'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = ('payment_sum', 'status', 'payment_type', 'created_at', 'updated_at')
    list_filter = ('status', 'payment_type')
