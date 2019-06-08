import random
import json
import csv

#people
class Person:
    def __init__(self,name):
        self.name = name

class Author(Person):
    def __init__(self, name):
        self.booksWritten = []
        super().__init__(name)

class Customer(Person):
    def __init__(self, number, gender, nameSet, givenName, surName, streetAddress, zipCode, city, emailAddress, username, telephoneNumber):
        self.number = number
        self.gender = gender
        self.nameSet = nameSet
        #self.givenName = givenName
        #self.surName = surName
        self.streetAddress = streetAddress
        self.zipCode = zipCode
        self.city = city
        self.emailAddress = emailAddress
        self.username = username
        self.telephoneNumber = telephoneNumber
        super().__init__(givenName+""+surName)


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
    def __init__(self):
        self.books = []
    
    def search(self, value):
        for items in self.books:
            if value == items.title:
                print(items.author.name)
            elif value == items.author:
                pass            

#loaning
class LoanAdministration:
    def __init__(self):
        self.allCustomers = []
        self.allBookitems = []

class LoanItem:
    def __init__(self):
        pass



catalog = Catalog()
loan_administration = LoanAdministration()
booksset1 = json.load(open('booksset1.json', 'r'))
FakeNameSet20 = csv.reader(open('FakeNameSet20.csv', 'r'), delimiter=',')

# next skipped de eerste rij in csv file wat namelijk de header van elke kolom is
next(FakeNameSet20)
for books in booksset1:
    books = Book(books['author'], books['country'], books['imageLink'], books['language'], books['link'], books['pages'], books['title'], books['year'])
    catalog.books.append(books)

for people in FakeNameSet20:
    customer = Customer(people[0],people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], people[10])
    loan_administration.allCustomers.append(customer)

#initializing the PLS
#for items in catalog.books:
#    print(items.title)
#print(loan_administration.allCustomers[0].city)
