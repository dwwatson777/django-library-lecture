from django.shortcuts import render
from django.http import HttpResponse
from book_app.models import Book
from book_app.forms import BookForm

def index(request):
    try:
        all_books = Book.objects.all() # SELECT * FROM book_app_book;
        my_data = {
            "books": all_books,
            "heading": "Hello World"
        }
        return render(request, "pages/index.html", context=my_data)

    except Exception as e:
        print(e)
        return HttpResponse("There was an error")


def book_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        my_data = {
            "b": book
        }
        return render(request, "pages/book_detail.html", context=my_data)
    except Exception as e:
        print(e)
        return HttpResponse("Page not found")


def book_create(request):
    try:
        print(request.method)
        # POST request
        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                print("form is valid")
                form.save()
            return HttpResponse(f"You added a new book {form.instance.title}")

        # GET request
        if request.method == "GET":
            form = BookForm()
            my_data = {
                "form": form
            }
            return render(request, "pages/book_form.html", context=my_data)
    except Exception as e:
        return HttpResponse("There was an error!!")



    


    
