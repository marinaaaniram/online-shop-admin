from django.urls import re_path
from orders.views import CreateOrderView

urlpatterns = [
    re_path('create', CreateOrderView.as_view(), name='CreateOrderView'),
]
