from django.shortcuts import render

from bookstore.models import Book
# Create your views here.


def all_book(request):
    books=Book.objects.all()
    return render(request,'bookstore/all_book.html',locals())