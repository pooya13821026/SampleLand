from django.db import models
from accounting.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', editable=False)
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت', editable=False)
    is_order_paid = models.BooleanField(verbose_name='پرداخت شده', editable=False)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return str(self.user)

    def total_price(self):
        total = 0
        if self.is_order_paid:
            for item in self.orderdetail_set.all():
                total += item.last_price * item.count
        else:
            for item in self.orderdetail_set.all():
                total += item.product.price * item.count
        return total


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    last_price = models.PositiveIntegerField(null=True, blank=True, verbose_name='قیمت نهایی محصول', editable=False)
    count = models.PositiveIntegerField(verbose_name='تعداد', editable=False)

    def getPriceCount(self):
        return self.product.price * self.count

    class Meta:
        verbose_name = 'جزئیات سفارش'
        verbose_name_plural = 'جزئیات سفارشات'

    def __str__(self):
        return str(self.order)
