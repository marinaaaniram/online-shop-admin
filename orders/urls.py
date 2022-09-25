from django.urls import re_path
from orders.views import CreateOrderView, ConfirmOrderView

urlpatterns = [
    re_path('create', CreateOrderView.as_view(), name='CreateOrderView'),
    re_path('confirm/(?P<order_id>\w+)', ConfirmOrderView.as_view(), name='ConfirmOrderView'),
]
