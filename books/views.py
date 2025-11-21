from django.shortcuts import render

from .models import Book,Author
# Create your views here.


def book_list(request):
    data = Book.objects.all()
    authers =Author.objects.all()
    return render(request,'books/all_books.html',{'books':data,'authers':authers})