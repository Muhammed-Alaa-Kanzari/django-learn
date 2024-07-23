
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view),
    path('books/', views.book_list, name='book-list'),
    path('books-search/', views.book_search, name='book-search'),
]
