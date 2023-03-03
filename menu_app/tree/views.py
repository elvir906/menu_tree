from django.views.generic import TemplateView

from .models import MenuItem


class HomePageView(TemplateView):
    """
    Класс для отображения первой страницы.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        items = MenuItem.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({
            'items': items
        })
        return context


class MenuItemView(TemplateView):
    """
    Класс для отображения всех страниц, кроме первой.
    """
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        """
        Функция, возвращающая контекст страницы
        """
        def sort_by_v_level(item):
            """
            Метод, указывающий на ключ при сортировке.
            Сортировка по абсолютному вертикальному уровню.
            """
            return item.v_level

        def tree_gen():
            """
            Метод, генерирующий дерево меню.
            """
            new_tree_list = []
            slug = self.kwargs.get("slug")

            items = MenuItem.objects.all()
            selected_item = MenuItem.objects.get(string=slug)

            for item in items:
                if (
                    item.h_level == 1
                    or (
                        (item.h_level < selected_item.h_level)
                        and (item.root_id == selected_item.root_id)
                    )
                    or (item.parent_id == selected_item.pk)
                    or (
                        (item.h_level == selected_item.h_level)
                        and (item.parent_id == selected_item.parent_id)
                    )
                ):
                    new_tree_list.append(item)
            new_tree_list.sort(key=sort_by_v_level)
            return new_tree_list

        context = super().get_context_data(**kwargs)
        context.update({
            'items': tree_gen(),
        })
        return context
