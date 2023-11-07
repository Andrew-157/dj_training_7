from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from django.db.models import Avg, Min, Max

from .models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'), Min('rating'), Max('rating'))
    return render(request, template_name='book_outlet/index.html',
                  context={'books': books,
                           'total_number_of_books': num_books,
                           'average_rating': avg_rating})


def book_detail(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    context = {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselling': book.is_bestselling
    }
    return render(request,
                  'book_outlet/book_detail.html',
                  context=context)
