from django.contrib import admin

from .models import Book, BookCategory, Library


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'shelf_number',
                    'book_number', 'isbn', 'is_returned']
    list_filter = ['author', 'shelf_number', 'is_returned']
    search_fields = ['name', 'author', 'book_number']

    class Meta:
        model = Book


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'incharge']
    list_filter = ['incharge']
    search_fields = ['name', 'incharge']


admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
