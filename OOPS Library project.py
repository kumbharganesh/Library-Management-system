''' Create a Library Class
Display Book
lend book=(who owns the book if not present)
add book
return book

GaneshLibrary= Library(listofbooks,library_name)

dictionary(books-name of person)

Create a main function and run an infinite while loop asking users for
their input '''

class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def display(self):
        print(f'We have following books in a library:{self.name}')
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender=Book Database has been updated.\n You can take the book now")
        else:
            print(f'Book is already being used by {self.lendDict[book]}')

    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)


G=Library(['Python','Rich Daddy','Harry potter','The ocean'],"ITLAB")

while(True):
    print(f'Welcome to the {G.name} library.Enter your choice to continue')
    print("1.Display Book")
    print("2.Lend a Book")
    print("3.Add a Book")
    print("4.Return a Book")
    user_choice=int(input())

    if user_choice==1:
        G.display()
        
    elif user_choice==2:
        book=input("Enter the name of the book you want to lend:")
        user=input("Enter your name:")
        G.lendBook(user,book)
        
    elif user_choice==3:
        book=input("Enter the name of the book you want to add:")
        G.addbook(book)
        
    elif user_choice==4:
        book=input("Enter the name of the book you want to return:")
        G.returnBook(book)
    else:
        print("Not a valid option")

    print("Press q to Quite and c to Continue")
    user_choice2=""
    while(user_choice2!="c" and user_choice2!="q"):
        user_choice2=input()
    if user_choice2=="q":
        exit()
    elif user_choice2=="c":
        continue
        
    
