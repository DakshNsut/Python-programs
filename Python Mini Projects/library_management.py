class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list(list_of_books)
        self.library_name = library_name
        self.list_of_available_books = list(list_of_books)
        self.Dict=dict()
    def __repr__(self):
        parts = []
        d = list(self.list_of_books)
        num = len(d)
        print(f"List of books you can lend from {self.library_name} are:")
        for i in range(num):
             print (d[i])
        return '\n'.join(parts)
    def __str__(self):
        parts = []
        d = list(self.list_of_available_books)
        num = len(d)
        print(f"List of available books you can lend from {self.library_name} are:")
        for i in range(num):
            print(d[i])
        return '\n'.join(parts)
    def list_calling(self):
        return self.list_of_available_books
    @property
    def add_book(self):
        a = input(f"Enter the name of book you want to add to the {self.library_name}.")
        return a
    @add_book.setter
    def add_book(self,st):
        self.list_of_available_books.append(st)
        self.list_of_books.append(st)

    @property
    def return_book(self):
        c = input(f"Enter the name of book you want to return to the {self.library_name}.")
        return c
    @return_book.setter
    def return_book(self, s):
        self.list_of_available_books.append(s)
        del self.Dict[s]
    @property
    def lend_book(self):
        parts = []
        d = list(self.list_of_books)
        num = len(d)
        print("Select the name of book you want to lend among the below books.")
        for i in range(num):
            print(d[i])
        return '\n'.join(parts)
    @lend_book.setter
    def lend_book(self,string):
        self.list_of_available_books.remove(string)
    @property
    def input_lender_name(self):
        name = input("What is your username?")
        return name
    @property
    def dict_lenders(self):
        return '\n'.join([])
    @dict_lenders.setter
    def dict_lenders(self,lists):
        key = lists[0]
        value = lists[1]
        self.Dict[key] = value
    def dict_printer(self):
        return self.Dict

if __name__ == '__main__':
    print("While working with the Library management system please take care that case of input should match with the instruction given\n")
    Harry_Library = Library(("Don Quixote", "A Tale of Two Cities", "The Lord of the Rings", "The Little Prince",
                             "Harry Potter and the Sorcerer's Stone"),"THE HARRY LIBRARY")
    TASK=input("Hey User!!!\nWhat do you want to do- Display all books,Display all available books,Lend a book,Return book or Add book\n:)")
    while(True):
        if TASK== "Display all books":
            repr(Harry_Library)
        elif TASK== "Display all available books":
            str(Harry_Library)
        elif TASK == "Add book":
            strings = Harry_Library.add_book
            Harry_Library.add_book = strings
            print("Book added successfully.")
        elif TASK == "Return book":
            stringd = Harry_Library.return_book
            Harry_Library.return_book = stringd
            print("Book returned successfully.")
        elif TASK == "Lend a book":
            str(Harry_Library.lend_book)
            stringl = input()
            o = Harry_Library.list_calling()
            if stringl in o:
                Harry_Library.lend_book = stringl
                stringn = Harry_Library.input_lender_name
                print("Book lent successfully")
                lists=[stringl,stringn]
                Harry_Library.dict_lenders=lists
            elif stringl not in o:
                dict11=Harry_Library.dict_printer()
                print(f"Book {stringl} not available. It is with person {dict11[stringl]}.")
            else:
                print("Invalid Input. Please try again.")
                TASK = input(
                    "\nHey User!!!\nWhat do you want to do- Display all books,Display all available books,Lend a book,Return"
                    " book or Add book\n:)")
                continue
        TASK = input("\nHey User!!!\nWhat do you want to do- Display all books,Display all available books,Lend a book,Return"
                     " book or Add book\n:)")
        continue