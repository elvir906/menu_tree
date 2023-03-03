[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

Задание:
-------

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

Описание:
-------

Тестовое задание выполнено на языке Python с использованием фреймворка Django. Запуск проекта производится с помощью Doсker. Так же использовал возможности Nginx для раздачи статики, чтобы Django-админка смотрелась презентабельней с DEBUG = False в settings.py. Бэкэнд-приложение и Nginx запускаются в двух разных контейнерах. Nginx и Django связываются благодаря Gunicorn.

Подготовка
------

Склонировать репозиторий на локальную машину
```
git clone https://github.com/elvir906/menu_tree.git
```

Запуск приложения в Docker
------
```
docker-compose up -d --build
```
Docker сам установит нужные зависимости из requirements.txt, запустит наше приложение
и серверные прилолжения Gunicorn и Nginx

Для отображения статики в админки выполнить
```
docker compose exec stripe-backend python manage.py collectstatic
```

Проект будет досупен по адресу http://127.0.0.1/.
Админка будет доступна по адресу http://127.0.0.1/admin/