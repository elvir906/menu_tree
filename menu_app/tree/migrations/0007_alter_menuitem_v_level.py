# Generated by Django 4.1.7 on 2023-03-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0006_menuitem_v_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='v_level',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Абсолютный уровень пункта по вертикали'),
        ),
    ]
