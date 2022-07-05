from django.contrib import admin

from app.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','description','category']
