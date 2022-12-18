class Book:
    def __init__(self, title, price, author, isbn):
        self.title = title
        self.price = price
        self.author = author
        self.isbn = isbn
        
    def info(self):
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        
def printMenu():
    print("1) 도서 추가 \n2) 도서 삭제 \n3) 도서 목록 출력 \n4) 종료 \n")
    n = int(input(">>  "))
    return n
    
def addBook():
    title = input("Title: ")
    price = input("Price: ")
    author = input("author: ")
    isbn = input("ISBN: ")
    book = Book(title, int(price), author, isbn)
    bookList.append(book)

def printBook(bookList):
    for i in bookList:
        print("-"*20)
        i.info()
    print("-"*20)
    
def delBook(bookList):
    isbn = input("ISBN >> ")
    bookList.pop()
        
bookList = []

def main():
    while True:
        menu = printMenu()
        if menu == 1:
            addBook()
        elif menu == 2:
            delBook(bookList)
        elif menu == 3:
            printBook(bookList)
        else:
            break
    
main()