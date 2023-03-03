from django import template

register = template.Library()


@register.simple_tag()
def tab(count):
    """
    Кастомный тэг, добавляющий отступ в строке для
    имитации раскрывающегося дерева пунктов меню
    """
    return (count - 1) * '    '
