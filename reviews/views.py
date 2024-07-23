from django.shortcuts import render
from .models import Book
from .utils import average_rating


def welcome_view(request):
    return render(request, 'reviews/base.html')


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({
            'book': book,
            'book_rating': book_rating,
            'number_of_reviews': number_of_reviews
        })

    context = {
        'book_list': book_list
    }
    print(request.GET)
    return render(request, 'reviews/book_list.html', context)


def book_search(request):
    search_text = request.GET.get('search', "")  # empty string
    context = {
        'search_text': search_text
    }
    return render(request, 'reviews/search-results.html', context)
