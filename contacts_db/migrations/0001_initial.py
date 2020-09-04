# Generated by Django 3.0.2 on 2020-09-04 00:09

import contacts_db.models
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.CharField(max_length=200)),
                ('business_type', models.CharField(blank=True, max_length=200)),
                ('discount_rate', models.FloatField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=contacts_db.models.business_content_file_name)),
            ],
            options={
                'verbose_name_plural': 'businesses',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=100)),
                ('socialmedia', models.CharField(max_length=100, verbose_name='Social Media')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_type', models.CharField(choices=[('home phone', 'Home Phone'), ('cell phone', 'Cell Phone'), ('work phone', 'Work Phone'), ('fax', 'Fax'), ('other', 'Other')], default='cell phone', max_length=20)),
                ('phonenumber', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('nickname', models.CharField(blank=True, max_length=200)),
                ('discount_rate', models.FloatField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=contacts_db.models.content_file_name)),
                ('is_tech', models.BooleanField(default=False, verbose_name='Technician?')),
                ('businesses', models.ManyToManyField(default='', related_name='contacts', to='contacts_db.Business')),
            ],
        ),
    ]
