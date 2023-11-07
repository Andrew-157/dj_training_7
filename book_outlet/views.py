from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


from .models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, template_name='book_outlet/index.html',
                  context={'books': books})
