# Generated by Django 4.2.5 on 2023-09-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], default='s', max_length=1, verbose_name='Тип'),
        ),
    ]