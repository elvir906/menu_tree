# Generated by Django 4.1.7 on 2023-03-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_remove_menuitem_v_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='v_level',
            field=models.IntegerField(default=0, verbose_name='Абсолютный уровень пункта по вертикали'),
        ),
    ]
