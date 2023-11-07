from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404


from .models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, template_name='book_outlet/index.html',
                  context={'books': books})


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
