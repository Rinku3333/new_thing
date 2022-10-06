class booklib:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybook(self):
        print(f"name of the books we have is :{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("dictionary has been updated, now u can take the book")

        elif book not in self.booklist(book):
            print("book is not in the library")

        else:
            print(f"book is already using by {self.lenddict[book]} , app kal aaana mast naha dho k ")

    def addbook(self,book):
        self.booklist.append(book)
        print("book has updated in the list")

    def returnbook(self,book):
        self.lenddict.pop(book)


if __name__=='__main__':
    thook = booklib( ['chacha choudhary','baal hans','mint ur money','goolmaal','hera pheri','hawasi yaar','mahaveer umang','freedom fighter ankit vasita'],"xyz" )

    while(True):
        print("choose 1,2,3,4 options as per ur requirement\n" )
        print("1:display books\n"
              "2:lend a book\n"
              "3:add a book\n"
              "4:return book\n")
        user_choice = int(input())

        if user_choice == 1:
            thook.displaybook()

        elif user_choice == 2:
            book = input("enter the name of the book u wanna to lend : ")
            user = input("enter your name : ")
            thook.lendbook(user,book)

        elif user_choice == 3:
            book = input("enter the name of the book : ")
            thook.addbook(book)

        elif user_choice == 4:
            book = input("enter the name of the book u wanna return : ")
            thook.returnbook(book)

        else:
            print("input is wrong pls reinput it\n")


        print("press q to quit and c to continue\n")
        user_choice1 = ""
        while(user_choice1 !='q' and user_choice1 !='c'):
            user_choice1 = input()
            if user_choice1 == 'q':
                exit()

            elif user_choice1 == 'c':
                continue



