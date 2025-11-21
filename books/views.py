from django.shortcuts import render

from .models import Book
# Create your views here.


def book_list(request):
    data = Book.objects.all()
    return render(request,'books/all_books.html',{'books':data})