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
        super().__init__(givenName+" "+surName)


    def loanBook(self,bookItem):
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
        self.copies = []
    
    def addCopy(self):
        self.copies.append(BookItem(self,False))
    
    def getAvailable(self):
        i = 0
        a = 0 #the amount of available copies
        while (i < len(self.copies)):
            if self.copies[i].loaned == False:
                a += 1
            i += 1
        return a
    
    def getTotalCopies(self):
        return len(self.copies)




# copies is het aantal exemplaren dat in de catlog zijn van een boek
class BookItem:
    def __init__(self,book,loaned):
        self.book = book
        self.loaned = loaned #of het wel of niet uigeleend is

class Catalog:
    def __init__(self):
        self.books = []
    
    def search(self, *value):
        bookList = []
        for value in value:
            for items in self.books:
                if value.lower() == items.title.lower():
                    bookList.append(items)
                elif value.lower() == items.author.name.lower():
                    bookList.append(items)
                elif value.lower() == items.country.lower():
                    bookList.append(items)
                elif value.lower() == items.language.lower():
                    bookList.append(items)
                elif str(value.lower()) == str(items.year):
                    bookList.append(items)
        bookset = list(set(bookList)) #bookset is is een set en sets dit zorgd voor geen dubble zoekresultaten bij meerdere zoek waarde
        for items in bookset:
            print("\nTitle: " + items.title + "\nAuthor: " + items.author.name + "\nLanguage: " + items.language + "\nYear " + str(items.year) + "\nPages: " + str(items.pages) + "\nAvailable copies: " + str(items.getTotalCopies()))

        

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
    i = random.randint(1,4)
    while i > 0:
        books.addCopy()
        i-=1
    catalog.books.append(books)

for people in FakeNameSet20:
    customer = Customer(people[0],people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], people[10])
    loan_administration.allCustomers.append(customer)

#initializing the PLS
# for items in catalog.books:
#     print(items.title)
#print(catalog.books[8])
#print(catalog.books[8].copies)
#print(catalog.books[8].copies[randint(0,len(catalog.books[10].copies)-1)].book.title)
#print(catalog.books[8].copies[0].book.title)
#print(catalog.books[8].copies[0].loaned)

# for i in catalog.books:
#     print(str(i.title)+" has "+str(i.getAvailable())+" copies available")

catalog.search("English", "Russian")
# print(catalog.search("to the lighthouse")[0].author.name)

