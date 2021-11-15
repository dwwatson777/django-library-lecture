from django.shortcuts import render, redirect
from django.http import HttpResponse
from book_app.models import Book
from book_app.forms import BookForm

def index(request):
    try:
        all_books = Book.objects.all().order_by("title") # SELECT * FROM book_app_book ORDER BY title
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
        # GET request
        if request.method == "GET":
            form = BookForm()
            my_data = {
                "form": form,
                "action": "Create"
            }
            return render(request, "pages/book_form.html", context=my_data)

        # POST request
        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                print("form is valid")
                form.save()
            return HttpResponse(f"You added a new book {form.instance.title}")

    except Exception as e:
        return HttpResponse("There was an error!!")


def book_update(request, book_id):
    try:
        # GET request
        book = Book.objects.get(id=book_id)
        if request.method == "GET":
            form = BookForm(instance=book)
            my_data = {
                "form": form,
                "action": "Update"
            }
            return render(request, "pages/book_form.html", context=my_data)

        # POST request
        if request.method == "POST":
            print(request.POST["title"])
            print(request.POST.keys())
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                print("form is valid")
                form.save()
            return redirect('book_detail', book_id=book_id)

    except Exception as e:
        return HttpResponse("There was an error!!")
    

def book_delete(request, book_id):
    try:
        # GET request
        book = Book.objects.get(id=book_id)
        if request.method == "GET":
            my_data = {
                "book": book
            }
            return render(request, "pages/book_delete.html", context=my_data)

        if request.method == "POST":
            Book.objects.get(id=book_id).delete()
            return redirect("book_list")
    except Exception as e:
        return HttpResponse("There was an error!!")