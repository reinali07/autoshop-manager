# Generated by Django 3.0.2 on 2020-09-06 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sup_invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryPart',
            fields=[
                ('part_number', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Internal Part Number')),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('min_stock', models.PositiveIntegerField()),
                ('full_stock', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, max_length=200)),
                ('average_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('area', models.CharField(blank=True, max_length=20)),
                ('row', models.CharField(blank=True, max_length=10)),
                ('line', models.CharField(blank=True, max_length=10)),
                ('interchangeable', models.CharField(blank=True, max_length=30, verbose_name='Interchangeable Part')),
                ('standard_unit', models.CharField(max_length=10)),
                ('sup_part', models.ManyToManyField(blank=True, related_name='internal', related_query_name='internal', to='sup_invoices.Part', verbose_name='part')),
            ],
            options={
                'verbose_name': 'Internal Part',
            },
        ),
    ]