# Generated by Django 4.2.9 on 2024-01-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciepe_name', models.CharField(max_length=100)),
                ('reciepe_description', models.TextField()),
                ('reciepe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
