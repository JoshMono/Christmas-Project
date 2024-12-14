# Generated by Django 5.1.4 on 2024-12-14 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_person_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_app.company'),
        ),
    ]
