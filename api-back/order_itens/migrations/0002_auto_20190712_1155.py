# Generated by Django 2.2.3 on 2019-07-12 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_itens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitens',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
        migrations.AlterField(
            model_name='orderitens',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]