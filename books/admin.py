from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import Author,Book,Review

admin.site.register(Author,SimpleHistoryAdmin)
admin.site.register(Book,SimpleHistoryAdmin)
admin.site.register(Review,SimpleHistoryAdmin)