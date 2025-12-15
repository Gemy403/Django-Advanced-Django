import graphene
from .models import Book,Author,Review
from graphene_django import DjangoObjectType

class AuthorsType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id','name','birth_date','bio','history')
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

class Query(graphene.ObjectType):
    authors = graphene.List(AuthorsType)
    books = graphene.List(BookType)
    ## update
    book = graphene.Field(BookType,book_id=graphene.ID(required=True))
    author = graphene.Field(AuthorsType,author_id=graphene.ID(required=True))

    
    def resolve_authors(self,info):
        return Author.objects.all()
    
    def resolve_books(self,info):
        return Book.objects.all()

    def resolve_book(self,info,book_id):
        return Book.objects.get(id=book_id)

    def resolve_author(self,info,author_id):
        return Author.objects.get(id=author_id)
    
schema = graphene.Schema(query=Query)