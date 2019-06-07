import random
import json

#people
class Person:
    def __init__(self,name):
        self.name = name
        self.books = []

class Author(Person):
    def __init__(self, name):
        super().__init__(name)

class Customer(Person):
    def __init__(self):
        pass


#books
class Book:
    def __init__(self,author,country,imageLink, language, link, pages, title, year):
        self.author = Author(author)
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year


class BookItem:
    def __init__(self,book):
        self.book = book

class Catalog:
    def __init__(self,books):
        self.books = books


#loaning
class LoanAdministration:
    def __init__(self):
        pass

class LoanItem:
    def __init__(self):
        pass



test = []
booksset1 = json.load(open('booksset1.json', 'r'))
for books in booksset1:
    books = Book(books['author'], books['country'], books['imageLink'], books['language'], books['link'], books['pages'], books['title'], books['year'])
    test.append(books)

#initializing the PLS
catalog = Catalog(test)
print(catalog.books[30].author.name)