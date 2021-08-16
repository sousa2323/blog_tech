from django.urls import path
from .views import IndexView, search_results

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', search_results, name='search_results'),
]
