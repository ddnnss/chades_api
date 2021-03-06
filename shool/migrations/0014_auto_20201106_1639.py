# Generated by Django 3.1.1 on 2020-11-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shool', '0013_callbackform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='bg_image',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='course', verbose_name='Картинка для бекграунда'),
        ),
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(null=True, upload_to='course', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='course',
            name='points_to_balance',
            field=models.IntegerField(null=True, verbose_name='Сколько балов после завершения курса'),
        ),
    ]
