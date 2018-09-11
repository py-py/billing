# Generated by Django 2.1.1 on 2018-09-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180911_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='client',
            field=models.BooleanField(default=True, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Деталировка компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование компании'),
        ),
        migrations.AlterField(
            model_name='legacyentity',
            name='document',
            field=models.CharField(max_length=255, verbose_name='На основании какого документа'),
        ),
        migrations.AlterField(
            model_name='legacyentity',
            name='first_name',
            field=models.CharField(max_length=32, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='legacyentity',
            name='last_name',
            field=models.CharField(max_length=32, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='legacyentity',
            name='patronymic',
            field=models.CharField(max_length=32, verbose_name='Отчествео'),
        ),
    ]
