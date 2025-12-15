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


class CreateBookMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        title = graphene.String(required=True)
        author_id = graphene.ID(required=True)
        publish_date = graphene.Date(required=True)
        price = graphene.Int(required=True)
    # The class attributes define the response of the mutation
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, title, author_id, publish_date, price):
        author = Author.objects.get(id=author_id)
        book = Book(
            title=title,
            author=author,
            publish_date=publish_date,
            price=price
            )
        book.save()
        return CreateBookMutation(book=book)


class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        bookid = graphene.ID(required=True)

        title = graphene.String()
        author_id = graphene.ID()
        publish_date = graphene.Date()
        price = graphene.Int()
    # The class attributes define the response of the mutation
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, bookid, **kwargs):
        book = Book.objects.get(id=bookid)
        for key,value in kwargs.items():
            if value is not None:
                setattr(book,key,value)
        book.save

        return UpdateBookMutation(book=book)


class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        bookid = graphene.ID(required=True)
    bookid = graphene.ID()
    def mutate(self, info, bookid, **kwargs):
        book = Book.objects.get(id=bookid)
        book.delete()
        return DeleteBookMutation(bookid=bookid)



class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()

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
    
schema = graphene.Schema(query=Query,mutation = Mutation)