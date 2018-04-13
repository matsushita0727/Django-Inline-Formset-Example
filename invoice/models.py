from django.contrib.auth.models import User
from django.core import validators
from django.db import models


class ItemGroup(models.Model):
    name = models.CharField(
        verbose_name='グループ名',
        max_length=100,
    )

    order = models.IntegerField(
        verbose_name='並び順',
        validators=[validators.MinValueValidator(0)],
    )

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100,
    )

    item_group = models.ForeignKey(
        ItemGroup,
        on_delete=models.CASCADE,
        verbose_name='グループ',
    )

    order = models.IntegerField(
        verbose_name='並び順',
        validators=[validators.MinValueValidator(0)],
    )

    price = models.IntegerField(
        verbose_name='単価',
        validators=[validators.MinValueValidator(0)],
    )

    def __str__(self):
        return self.name


class Invoice(models.Model):
    title = models.CharField(
        verbose_name='タイトル',
        max_length=100,
    )

    sub_total = models.IntegerField(
        verbose_name='小計',
    )

    tax = models.IntegerField(
        verbose_name='消費税',
    )

    total_amount = models.IntegerField(
        verbose_name='合計金額',
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='作成者',
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class InvoiceDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    price = models.IntegerField(
        verbose_name='単価',
        validators=[validators.MinValueValidator(0)],
    )

    quantity = models.IntegerField(
        verbose_name='数量',
        validators=[validators.MinValueValidator(0)],
    )

    amount = models.IntegerField(
        verbose_name='金額',
    )
