# Generated by Django 3.1.6 on 2021-02-06 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210206_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-date']},
        ),
    ]
