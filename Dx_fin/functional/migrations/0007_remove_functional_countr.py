# Generated by Django 4.2.1 on 2023-06-05 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('functional', '0006_functional_countr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functional',
            name='countr',
        ),
    ]
