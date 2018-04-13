# Generated by Django 2.0.4 on 2018-04-13 06:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('sub_total', models.IntegerField(verbose_name='税抜合計')),
                ('tax', models.IntegerField(verbose_name='消費税')),
                ('total_amount', models.IntegerField(verbose_name='税込合計')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='数量')),
                ('amount', models.IntegerField(verbose_name='小計')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('order', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='並び順')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='グループ名')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.ItemGroup', verbose_name='グループ'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Item'),
        ),
    ]
