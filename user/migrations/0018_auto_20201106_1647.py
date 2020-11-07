# Generated by Django 3.1.1 on 2020-11-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20201106_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Эл. почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ник'),
        ),
        migrations.AlterField(
            model_name='user',
            name='vi_chat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='vichat'),
        ),
    ]