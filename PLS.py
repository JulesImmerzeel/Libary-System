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
        self.myLoans = []
        super().__init__(givenName+" "+surName)


    def loanBook(self, Book):

        if Book.getAvailable() > 0:
            for books in Book.copies:
                if books.loaned == False:
                    books.loaned = True
                    loan_administration.allLoanedItems.append(LoanItem(self.name, books))
                    self.myLoans.append(books)
                    print("\nDear " + self.name + ", \nYou loaned: \nTitle: " + Book.title + "\nAuthor: " + Book.author.name + "\nLanguage: " + Book.language + "\nYear " + str(Book.year) + "\nPages: " + str(Book.pages))
                    break
        else:
            print('all copies are loaned out')

    

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
    #function to add bookItems
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

class BookItem:
    def __init__(self,book,loaned):
        self.book = book
        self.loaned = loaned #of het wel of niet uigeleend is

class Catalog:
    def __init__(self):
        self.books = []
    # searching in catalog
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
        bookList = list(set(bookList)) #bookset is is een set en sets dit zorgd voor geen dubble zoekresultaten bij meerdere zoek waarde
        b = 0
        for items in bookList:
            print("book nr "+str(b)+"\nTitle: " + items.title + "\nAuthor: " + items.author.name + "\nLanguage: " + items.language + "\nYear " + str(items.year) + "\nPages: " + str(items.pages) + "\nAvailable copies: " + str(items.getTotalCopies()))
        print("end of list")
        return bookList

        

#loaning
class LoanAdministration:
    def __init__(self):
        self.allCustomers = []
        self.allBookitems = []
        self.allLoanedItems = []
    
    def addNewCustomer(self, customer):
        return self.allCustomers.append(customer)

class LoanItem:
    def __init__(self, customer, bookItem):
            self.customer = customer
            self.bookItem = bookItem



catalog = Catalog()
loan_administration = LoanAdministration()
# filling with books
booksset1 = json.load(open('booksset1.json', 'r'))
# filling with customers
FakeNameSet20 = csv.reader(open('FakeNameSet20.csv', 'r'), delimiter=',')

# next skipped de eerste rij in csv file wat namelijk de header van elke kolom is
next(FakeNameSet20)

# adding books
for books in booksset1:
    books = Book(books['author'], books['country'], books['imageLink'], books['language'], books['link'], books['pages'], books['title'], books['year'])
    i = random.randint(1,4)
    while i > 0:
        books.addCopy()
        i-=1
    catalog.books.append(books)

# adding customers
for people in FakeNameSet20:
    loan_administration.addNewCustomer(Customer(people[0],people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], people[10]))


print(catalog.books[10].getAvailable())
loan_administration.allCustomers[10].loanBook(catalog.books[10])
print(loan_administration.allLoanedItems)
print(catalog.books[10].getAvailable())
loan_administration.allCustomers[10].loanBook(catalog.books[10])
print(loan_administration.allLoanedItems)
print(catalog.books[10].getAvailable())
loan_administration.allCustomers[10].loanBook(catalog.books[10])
print(loan_administration.allLoanedItems)
print(catalog.books[10].getAvailable())
loan_administration.allCustomers[10].loanBook(catalog.books[10])
print(loan_administration.allLoanedItems)
print(catalog.books[10].getAvailable())
loan_administration.allCustomers[10].loanBook(catalog.books[10])
print(loan_administration.allLoanedItems)
print(catalog.books[10].getAvailable())
