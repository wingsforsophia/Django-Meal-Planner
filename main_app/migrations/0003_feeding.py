# Generated by Django 3.1.6 on 2021-02-06 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_plan_end'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='meal date')),
                ('name', models.CharField(max_length=100)),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='D', max_length=1)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plan')),
            ],
        ),
    ]
