from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import JsonResponse

from .models import Order
from .decorators import basicauth

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'amount']


def orders_list(request, template_name='orders/orders_list.html'):
    orders = Order.objects.all()
    data = {'object_list': orders}
    return render(request, template_name, data)


def order_create(request, template_name='orders/order_form.html'):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders:orders_list')
    return render(request, template_name, {'form': form})


def order_update(request, pk, template_name='orders/order_form.html'):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('orders:orders_list')
    return render(request, template_name, {'form': form})


def order_delete(request, pk, template_name='orders/order_confirm_delete.html'):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:orders_list')
    return render(request, template_name, {'object': order})


@basicauth
def export_orders(request):
    orders = Order.objects.all().values('customer', 'amount', 'date')
    result = {'result': list(orders)}
    return JsonResponse(result)

