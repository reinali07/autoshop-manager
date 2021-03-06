# Generated by Django 3.0.2 on 2020-09-06 01:15

import clientcars_db.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles_db', '0001_initial'),
        ('contacts_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('vin', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', message='VIN is alphanumeric')], verbose_name='VIN')),
                ('licenseplate', models.CharField(blank=True, max_length=15, verbose_name='License Plate')),
                ('comments', models.TextField(blank=True, max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('colour', models.CharField(choices=[('black', 'Black'), ('blue', 'Blue'), ('brown', 'Brown'), ('red', 'Red'), ('silver', 'Silver'), ('white', 'White'), ('yellow', 'Yellow'), ('uk', '--')], default='uk', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=clientcars_db.models.content_file_name)),
                ('clientcontact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts_db.Contact', verbose_name='Owner')),
                ('clientvehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='vehicles_db.Vehicle', verbose_name='Vehicle')),
            ],
        ),
    ]
