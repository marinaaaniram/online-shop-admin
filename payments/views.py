from django.http import JsonResponse
from rest_framework.views import APIView
from orders.models import Order
from payments.models import Payment
from payments.serializers import PaymentSerializer


class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        order_id = data.get('order_id')

        if order_id and isinstance(order_id, int):
            try:
                order = Order.objects.get(id=order_id)
                payment, created = Payment.objects.get_or_create(
                    order=order,
                    payment_sum=order.order_sum,
                )
                if created:
                    payment.payment_sum = order.order_sum
                    payment.save()
                else:
                    return JsonResponse({'status': 'error', 'msg': 'You\'re repeating yourself'})
                return JsonResponse({'status': 'ok', 'payment': PaymentSerializer(payment).data})
            except Order.DoesNotExist:
                return JsonResponse({'status': 'error', 'msg': 'Error order'})

        return JsonResponse({'status': 'error', 'msg': 'Something went wrong!'})


