from django.contrib import admin

# Register your models here.
from .models import Author,Book,Review


class BookAdmin(admin.ModelAdmin):
    list_display=['title','price','formated_price']


admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(Review)