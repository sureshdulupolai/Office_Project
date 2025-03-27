# Generated by Django 5.1.6 on 2025-03-22 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='profile/')),
                ('desc', models.TextField(blank=True, max_length=5000, null=True)),
                ('nich_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(max_length=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
