import random
import json
import csv
#people
class Person:
    def __init__(self,name):
        self.name = name

class Author(Person):
    def __init__(self, name):
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


    def loanBook(self, Book):
        if Book.getAvailable() > 0:
            for books in Book.copies:
                if books.loaned == False:
                    books.loaned = True
                    loan_administration.allLoanedItems.append(LoanItem(self.name, books))
                    print("Dear " + self.name + ", \nYou loaned: \nTitle: " + Book.title + "\nAuthor: " + Book.author.name + "\nLanguage: " + Book.language + "\nYear " + str(Book.year) + "\nPages: " + str(Book.pages))
                    break
        else:
            print('all copies are loaned out')

    def loanBook(self, Book):

        if Book.getAvailable() > 0:
            for books in Book.copies:
                if books.loaned == False:
                    books.loaned = True
                    loan_administration.allLoanedItems.append(LoanItem(self.name, books))
                    print("\nDear " + self.name + ", \nYou loaned: \nTitle: " + Book.title + "\nAuthor: " + Book.author.name + "\nLanguage: " + Book.language + "\nYear " + str(Book.year) + "\nPages: " + str(Book.pages))
                    break
        else:
            print('all copies are loaned out')
    
    def returnBook(self,loanItem):
        for item in loan_administration.allLoanedItems:
            if item == loanItem:
                loanItem.bookItem.loaned = False
                loan_administration.allLoanedItems.remove(loanItem)
                break


#books
class Book:
    def __init__(self,author,country,imageLink, language, link, pages, title, year):
        if author in catalog.authors:
            self.author = catalog.authors[author]
        else:
            self.author = Author(author)
            catalog.authors[author] = self.author
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
        self.books = {}
        self.authors = {}
    # searching in catalog
    def search(self, *value):
        bookList = []
        for value in value:
            value = str(value)
            for items in self.books.values():
                if value.lower() in items.title.lower():
                    bookList.append(items)
                elif value.lower() in items.author.name.lower():
                    bookList.append(items)
                elif value.lower() in items.country.lower():
                    bookList.append(items)
                elif value.lower() in items.language.lower():
                    bookList.append(items)
                elif value.lower() == items.year:
                    bookList.append(items)
        bookList = list(set(bookList)) #bookset is is een set en sets dit zorgd voor geen dubble zoekresultaten bij meerdere zoek waarde
        for items in bookList:
            print("\nTitle: " + items.title + "\nAuthor: " + items.author.name + "\nLanguage: " + items.language + "\nYear " + str(items.year) + "\nPages: " + str(items.pages) + "\nAvailable copies: " + str(items.getTotalCopies()))

        

#loaning
class LoanAdministration:
    def __init__(self):
        self.allCustomers = {}
        self.allBookitems = {}
        self.allLoanedItems = []

    def addNewCustomer(self, number, gender, nameSet, givenName, surName, streetAddress, zipCode, city, emailAddress, username, telephoneNumber):
        self.allCustomers[givenName+" "+surName] = Customer(number, gender, nameSet, givenName, surName, streetAddress, zipCode, city, emailAddress, username, telephoneNumber)
        
    def makeBackup(self):
        backupFile = open("backupFile.json","w+")
        listCustomers = []
        for key, value in self.allCustomers.items():
            data = value.__dict__
            listCustomers.append(data)

        listBookItems = []
        for key, value in catalog.books.items():
            value.author = value.author.name
            value.copies = len(value.copies)
            data = value.__dict__
            listBookItems.append(data)
        
        listLoanItems = []
        for value in self.allLoanedItems:
            # value.customer = self.allCustomers[value.customer['name']]
            value = [value.bookItem.book.title, value.customer]
            listLoanItems.append(value)
        all = [listCustomers, listBookItems, listLoanItems]
        json.dump(all, backupFile)
        
        backupFile.close()

    def restoreFromBackup(self):
        backupFilejson = open("backupFile.json","r")
        backupFile = json.load(backupFilejson)
        self.allCustomers.clear()
        for items in backupFile[0]:
            self.addNewCustomer(items["number"],items["gender"], items["nameSet"], items["name"].split()[0], items["name"].split()[1], items["streetAddress"], items["zipCode"], items["city"], items["emailAddress"], items["username"], items["telephoneNumber"])
        
        catalog.books.clear()
        for items in backupFile[1]:
            book = Book(items['author'], items['country'], items['imageLink'], items['language'], items['link'], items['pages'], items['title'], items['year'])
            catalog.books[items["title"]] = book
        
            i = items['copies']
            while i > 0:
                book.addCopy()
                i -= 1
        self.allLoanedItems.clear()
        print(self.allLoanedItems)
        for items in backupFile[2]:
            book = LoanItem(self.allCustomers[items[1]], catalog.books[items[0]])
            self.allLoanedItems.append(book)
        backupFilejson.close()

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
    catalog.books[books.title] = books

# adding customers
for people in FakeNameSet20:
    loan_administration.addNewCustomer(people[0],people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], people[10])

loan_administration.allCustomers['Valentin Bosgra'].loanBook(catalog.books['Fairy tales'])
loan_administration.makeBackup()
print(loan_administration.allLoanedItems)
loan_administration.restoreFromBackup()
print(loan_administration.allLoanedItems)

print(loan_administration.allLoanedItems)
