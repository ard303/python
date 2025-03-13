class library:
    def __init__(self,list_of_books,name):
        self.bookList=list_of_books
        self.name=name
        self.lendDict={}


    def  displayBooks(self):
       print(f"We have the following books in our library : {self.name}")
       for book in self.bookList:
        print(book)

    def  lendBook(self,user,book):
            if book not in self.bookList:
                print("sorry we dont have this book")
            elif book in self.lendDict:
                print("this book is already being used by someone")
            else:
                self.lendDict[book]=user
                print("you can take this book")

    def addBook(self,book):
        self.bookList.append(book)
        print(f"{book} has beeen added to library")    

    def returnBook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("book has been returned")
        else:
            print("this book was not borrowed from us")   

if __name__=='__main__':
    books=library(['harry potter','ace of spades','shadowhunters','six of crows','daughter of the deep'] ,"Let's Upskill")

    user_name=input("welxome to our library. Please enter your name :")

    while True:
        print(f" \n hello {user_name}, welcome to the {books.name} please choose an option: ")
        print("\n 1.display books \n 2.lend a book \n 3.add a book \n 4.return a book \n 5.quit")
        user_choice=input("enter your choice to continue :")
        if user_choice not in ['1','2','3','4','5']:
            print("please enter a valid input")
            continue
        if user_choice=='1':
            books.displayBooks()
        elif user_choice=='2':
            book=input("enter the book that you want to lend")
            books.lendBook(user_name,book)
        elif user_choice=='3':
            bookadd=input("enter the book that you want to add")
            books.addBook(bookadd)
        elif user_choice=='4':
            bookreturn=input("enter the book that you want to return")
            books.returnBook(bookreturn)
        else:
            print("good bye")
            break    

      
                  

