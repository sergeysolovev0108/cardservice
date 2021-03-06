# Generated by Django 3.1.1 on 2020-09-01 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activedate',
            options={'verbose_name': 'Пополнение карт', 'verbose_name_plural': 'Пополнение карт'},
        ),
        migrations.AlterModelOptions(
            name='cardcategory',
            options={'verbose_name': 'Категории карт', 'verbose_name_plural': 'Категории карт'},
        ),
        migrations.AlterModelOptions(
            name='cardstatus',
            options={'verbose_name': 'Статусы карт', 'verbose_name_plural': 'Статусы карт'},
        ),
        migrations.AlterModelOptions(
            name='clubcard',
            options={'verbose_name': 'Карты', 'verbose_name_plural': 'Карты'},
        ),
        migrations.AlterModelOptions(
            name='sex',
            options={'verbose_name': 'Пол', 'verbose_name_plural': 'Пол'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.RenameField(
            model_name='sex',
            old_name='title',
            new_name='gender',
        ),
    ]
