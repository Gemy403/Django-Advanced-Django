from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
import random
from books.models import Author,Book,Review

class Command(BaseCommand):
    help = 'Generate Random Dummy Data'

    def add_arguments(self, parser):
        parser.add_argument('authers',type=int,default=10,help='number of dummy authers to generate, default =10')
        parser.add_argument('books',type=int,default=20,help='number of dummy books to generate, default =20')
        parser.add_argument('reviews',type=int,default=50,help='number of dummy reviews to generate, default =50')
    
    def handle(self, *args, **options):
        num_authers = options['authers']
        num_books = options['books']
        num_reviews = options['reviews']

        self.generate_authors(num_authers)
        self.generate_books(num_books)
        self.generate_reviews(num_reviews)


    def generate_authors(self,num_authers):
        fake = Faker()
        for _ in range (num_authers):
            author = Author.objects.create(
                name = fake.name(),
                birth_date = fake.date_of_birth(minimum_age = 20,maximum_age=60),
                bio = fake.paragraph(nb_sentences=4)
            )
            author.save()
        print(f'Num authers was created Successfuly : {num_authers}')

    def generate_books(self,num_books):
        fake = Faker()
        authors = Author.objects.all()
        for _ in range(num_books):
            book = Book.objects.create(
                title = fake.sentence(nb_words=5),
                author = fake.random_element(authors),
                publish_date = fake.date_this_century(before_today=True,after_today=False),
                price = fake.pydecimal(min_value=25,max_value=100,right_digits=2)

            )
            book.save()

        print(f'Num books was created Successfuly : {num_books}')

    def generate_reviews(self,num_reviews):
        fake = Faker()
        books = Book.objects.all()
        print('(num_reviews)//len(books)',len(books)//(num_reviews))
        for book in books:
            for _ in range((num_reviews)//len(books)):
                review = Review.objects.create(
                    book = book,
                    reviewer_name = fake.name(),
                    review = fake.paragraph(nb_sentences=5),
                    rate = fake.random_int(min=1,max=5),

                )
                review.save()
        print(f'Num reviews was created Successfuly : {num_reviews}')
