from django.urls import path

from .views import HomePageView, MenuItemView

app_name = 'tree'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path(r'<slug:slug>/', MenuItemView.as_view(), name='menu_item'),
]
