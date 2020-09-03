# Generated by Django 3.0.6 on 2020-07-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200702_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do cliente')),
                ('payment', models.CharField(max_length=50, verbose_name='Meio Pagamento')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]