# Generated by Django 5.1.4 on 2024-12-14 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name='First Name')),
                ('last_name', models.TextField(verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]