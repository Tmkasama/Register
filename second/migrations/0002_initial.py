# Generated by Django 5.0.1 on 2024-01-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('second', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subtotal', models.CharField(max_length=20)),
                ('Taxes', models.CharField(max_length=20)),
                ('Shipping', models.CharField(max_length=20)),
                ('Total', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_drop_off', models.BooleanField(default=False)),
                ('local_pick_up', models.BooleanField(default=False)),
                ('shopping', models.BooleanField(default=False)),
                ('ship_N', models.CharField(max_length=10)),
                ('ship_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.BooleanField(default=False)),
                ('card', models.BooleanField(default=False)),
                ('checks', models.BooleanField(default=False)),
                ('paypal', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
