from django.db import models


class MenuItem(models.Model):
    string = models.CharField(
        max_length=100,
        verbose_name='Строка дерева'
    )
    h_level = models.IntegerField(
        verbose_name='Уровень пункта по горизонтали',
        default=0
    )
    v_level = models.DecimalField(
        verbose_name='Абсолютный уровень пункта по вертикали',
        default=0,
        max_digits=4,
        decimal_places=2
    )
    parent_id = models.IntegerField(
        verbose_name='id родителя',
        default=0
    )
    root_id = models.IntegerField(
        verbose_name='id_прародителя',
        default=0
    )
