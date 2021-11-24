from django.db import models
from django.urls import reverse

from customers.models import Customer


class Order(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    amount = models.IntegerField(verbose_name='amount')
    customer = models.ForeignKey(Customer, verbose_name='customer',
                                 on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.customer.name

    def get_absolute_url(self):
        return reverse('orders:order_edit', kwargs={'pk': self.pk})
