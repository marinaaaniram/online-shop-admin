from django.urls import re_path
from orders.views import CreateOrderView
from payments.views import CreatePaymentView

urlpatterns = [
    re_path('create', CreatePaymentView.as_view(), name='CreatePaymentView'),
]
