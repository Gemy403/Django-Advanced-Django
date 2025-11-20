
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from books.models import Author,Book,Review
from faker import Faker
from typer import Typer

app = Typer()

def generate_authers(num_authers):
    print('Generating Authers')
    fake = Faker()
    authers = []
    for _ in range (num_authers):
        author = Author.objects.create(
            name = fake.name(),
            birth_date = fake.date_of_birth(minimum_age = 20,maximum_age=60),
            bio = fake.paragraph(nb_sentences=4)
        )
        author.save()
        authers.append(author)
    return authers




@app.command()
def generate_all_authors(num_authers:int = 10):
    authors = generate_authers(num_authers)

####

def generate_books(authors,num_books):
    print('Generating Books')
    fake = Faker()
    books =[]
    for _ in range(num_books):
        book = Book.objects.create(
            title = fake.sentence(nb_words=5),
            author = fake.random_element(authors),
            publish_date = fake.date_this_century(before_today=True,after_today=False),
            price = fake.pydecimal(min_value=25,max_value=100,right_digits=2)

        )
        book.save()
        books.append(book)
    return books


@app.command()
def generate_all_books(num_bookd:int = 20):
    authors = Author.objects.all()
    bookd = generate_books(authors,num_bookd)


####
def generate_reviews(books,num_reviews):
    print('Generating Reviews')
    fake = Faker()
    reviews =[]
    for book in books:
        for _ in range((num_reviews)//len(books)):
            review = Review.objects.create(
                book = book,
                reviewer_name = fake.name(),
                review = fake.paragraph(nb_sentences=5),
                rate = fake.random_int(min=1,max=5),

            )
            review.save()
            reviews.append(review)
    # return reviews

@app.command()
def generate_all_reviews(num_reviews:int = 50):
    books = Book.objects.all()
    generate_reviews(books,num_reviews)


@app.command()
def generate_dummy_data(num_authers:int=10, num_books:int=20, num_reviews:int=50):
    generate_all_authors(num_authers)
    generate_all_books(num_books)
    generate_all_reviews(num_reviews)

if __name__ == '__main__':
    app()