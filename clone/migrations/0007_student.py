# Generated by Django 4.2.11 on 2024-04-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0006_car_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.ImageField(upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
