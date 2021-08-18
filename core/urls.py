from django.urls import path
from .views import IndexView, search_results, search_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search_view/<int:search_id>', search_view, name='search_view'),
    path('search/', search_results, name='search_results'),
]
