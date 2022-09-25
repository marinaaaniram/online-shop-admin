import requests
from django.db.models import Sum
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView

from online_shop_admin.settings import WEBHOOK_SITE
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


class ConfirmOrderView(APIView):
    def get(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                if order.payment.PAID:
                    order.status = Order.CONFIRMED
                    order.confirmed_at = timezone.now()
                    order.save()

                    try:
                        requests.post(WEBHOOK_SITE, json={
                            'id': order.id,
                            'amount': order.order_sum,
                            'date': order.confirmed_at.strftime('%d/%m/%Y, %H:%M:%S'),
                        })
                    except requests.exceptions.RequestException as e:
                        raise SystemExit(e)

                return JsonResponse({'status': 'ok', 'payment': OrderSerializer(order).data})
            except Order.DoesNotExist:
                return JsonResponse({'status': 'error', 'msg': 'Error order'})

        return JsonResponse({'status': 'error', 'msg': 'Something went wrong!'})



