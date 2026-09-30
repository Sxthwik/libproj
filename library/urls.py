from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
