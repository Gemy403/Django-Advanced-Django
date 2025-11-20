
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from books.models import Author,Book,Review
from faker import Faker
from typer import Typer

app = Typer()

def generate_authers(num_authers):
    print('generating authers')

@app.command()
def generate_all_authors(num_authers:int = 10):
    authors = generate_authers(num_authers)



def generate_books(authors,num_books):
    pass

@app.command()
def generate_all_books(num_bookd:int = 20):
    authors = Author.objects.all()
    bookd = generate_books(authors,num_bookd)



def generate_reviews(books,num_reviews):
    pass

@app.command()
def generate_reviews(num_reviews:int = 50):
    books = Book.objects.all()
    generate_reviews(books,num_reviews)




if __name__ == '__main__':
    app()