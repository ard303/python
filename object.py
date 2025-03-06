class library:
    def __init__(self,list_of_books,name):
        self.bookList=list_of_books
        self.name=name
        self.lendDict={}


    def  displayBooks(self):
       print(f"We have the following books in our library : {self.name}")
       for book in self.booksList:
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
                  

