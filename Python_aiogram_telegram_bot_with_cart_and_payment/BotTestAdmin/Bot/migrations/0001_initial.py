# Generated by Django 4.1.5 on 2023-02-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='ID пользователя')),
                ('prod_id', models.IntegerField(verbose_name='ID продукта')),
                ('quantity', models.IntegerField(verbose_name='Количество продукта')),
            ],
            options={
                'verbose_name': 'Таблица корзин пользователей',
                'verbose_name_plural': 'Таблица корзин пользователей',
                'db_table': 'cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID продукта')),
                ('prod_name', models.TextField(blank=True, null=True, verbose_name='Название продукта')),
                ('prod_description', models.TextField(blank=True, null=True, verbose_name='Описание продукта')),
                ('prod_price', models.IntegerField(verbose_name='Цена продукта')),
                ('prod_photo', models.IntegerField(blank=True, null=True, verbose_name='ID фото продукта')),
            ],
            options={
                'verbose_name': 'Таблица каталога',
                'verbose_name_plural': 'Таблица каталога',
                'db_table': 'catalog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID пользователя')),
                ('user_name', models.TextField(verbose_name='Имя пользователя')),
                ('user_surname', models.TextField(blank=True, null=True, verbose_name='Фамилия пользователя')),
                ('username', models.TextField(blank=True, null=True, verbose_name='Никнейм пользователя')),
                ('active', models.IntegerField(blank=True, null=True, verbose_name='Состояние активности пользователя')),
                ('user_phone', models.IntegerField(blank=True, null=True, verbose_name='Телефон пользователя')),
            ],
            options={
                'verbose_name': 'Пользователи бота',
                'verbose_name_plural': 'Пользователи бота',
                'db_table': 'people',
                'managed': False,
            },
        ),
    ]
