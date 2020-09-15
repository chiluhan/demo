from django.urls import path

# from . import views
# from mysite3.bookstore import views
from bookstore import views

urlpatterns = [
    # http://127.0.0.1:8000/bookstore/all_book
    path('all_book',views.all_book)
    ]