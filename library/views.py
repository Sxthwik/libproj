from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(view_self):
    books = Book.objects.all()
    form = BookForm()
    if view_self.method == 'POST':
        form = BookForm(view_self.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    return render(view_self, 'library/book_list.html', {'books': books, 'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
