from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import *

# Create your models here.
class Author(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    birth_date = models.DateField(_("Birth Date"), )
    bio = models.TextField(_("Bio"),max_length=500)
    def __str__(self):
        return self.name
    
    def age(self):
        today = date.today()
        age =  today.year - self.birth_date.year
        return age


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    author = models.ForeignKey(Author, verbose_name=_("Author"), on_delete=models.CASCADE,related_name='book_author')
    publish_date = models.DateField(_("Publish Date"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2) 
   
    def __str__(self):
        return self.title
    
    @property
    def formated_price(self):
        return f"${self.price}"
    
class Review(models.Model):
    book = models.ForeignKey(Book, verbose_name=_("Book"),related_name='review_book', on_delete=models.CASCADE)
    reviewer_name = models.CharField(_("Reviewr Name"), max_length=100)
    review = models.TextField(_("Review"),max_length=500)
    rate = models.IntegerField(_("Rate"),choices=[(i,i)for i in range(1,6)])

    def __str__(self):
        return f"Review of {self.book} for {self.reviewer_name}"