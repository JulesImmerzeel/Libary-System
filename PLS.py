import random
import json

#people
class Person:
    def __init__(self,name):
        self.name = name
        self.books = []

class Author(Person):
    def __init__(self):

class Customer(person):
    def __init__(self):


#books
class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

class BookItem:
    def __init__(self,book):
        self.book = book

class Catalog:
    def __init__(self,books):
        self.books = books

#loaning
class LoanAdministration:
    def __init__(self):

class LoanItem:
    def __init__(self):

#initializing the PLS

catalog = Catalog([Book])
