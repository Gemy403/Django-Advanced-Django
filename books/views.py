from django.shortcuts import render
from .models import Author,Book,Review
from django.core.paginator import Paginator


# Create your views here.
def all_history(request):
    authors = Author.history.all()
    books = Book.history.all()
    reviews = Review.history.all()

    history = list(authors) + list(books) + list(reviews)

    # Sort by date DESC
    history.sort(key=lambda x: x.history_date, reverse=True)

    # Add model name manually because templates cannot access _meta
    for item in history:
        item.model_name = item.instance.__class__.__name__
        print('item.model_name',item.model_name)

    # Pagination
    paginator = Paginator(history, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "books/all_history.html", {
        "page_obj": page_obj,
    })