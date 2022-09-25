from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.views import APIView

from orders.models import Order
from orders.serializers import OrderSerializer
from products.models import Product


class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        products_list_ids = data.get('products_list_ids')

        if products_list_ids and isinstance(products_list_ids, list):
            products_queryset = Product.objects.filter(id__in=products_list_ids)
            order_sum = products_queryset.aggregate(order_sum=Sum('price'))['order_sum']

            order = Order.objects.create(order_sum=order_sum)
            order.products.add(*products_queryset)
            return JsonResponse({'status': 'ok', 'order': OrderSerializer(order).data})

        return JsonResponse({'status': 'error', 'msg': 'Something went wrong!'})


