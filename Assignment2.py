"""LIBRARY MANAGEMENT SYSTEM"""

class Library:

    def __init__(self, book_list, name):
        self.book_list = book_list
        self.lib_name = name
        self.book_lending_dict = {}

    def display_books(self):
        for book in self.book_list:
            print(book)

    def lending_books(self, user_name, book):
        if book not in self.book_lending_dict.keys():
            print("You request for lending this book granted. Your details updated successfully.")
            self.book_lending_dict.update({book:user_name})
        else:
            print(f"This book was already taken by {self.book_lending_dict[book]}.You can wait till availability or lend a another book.")

    def donating_books(self, book):
        print("Thank you for your support.")
        self.book_list.append(book)

    def returning_book(self, book):
        print("Thank you for co-operating with us")
        self.book_lending_dict.pop(book)


if __name__ == '__main__':
    hrithik = Library(["GAME OF THRONES", "PRINCE OF PERSIA","LORDS OF RINGS","HARRY POTTER","ICE AGE"], "Hrithik")

    while True:
        print(f"Welcome to {hrithik.lib_name} online Library")
        print("What do you want to do?")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Donate a book")
        print("4. Return a book")
        person_choice_1 = input("Select any option : ")
        if person_choice_1 not in ["1","2","3","4"]:
            print("Wrong input.Try again.")
            continue
        else:
            person_choice_1 = int(person_choice_1)
        if person_choice_1 == 1:
            print(hrithik.display_books())
        elif person_choice_1 == 2:
            book = input("Which book want to lend?\n")
            user_name = input("Enter your ID name: ")
            hrithik.lending_books(user_name.upper(),book.upper())
        elif person_choice_1 == 3:
            book = input("Write name of the book you wanted to donate: ")
            hrithik.donating_books(book.upper())
        elif person_choice_1 == 4:
            book = input("Write name of the book you wanted to return: ")
            hrithik.returning_book(book.upper())

        print("Print Q to quit and C to continue.")
        user_choice_2 = input("Choose any option :")
        while user_choice_2 != "c" and user_choice_2 != "q":
            print("Wrong input.Try again.")
            user_choice_2 = input("Choose any option :")
            continue
        if user_choice_2.upper() == "Q":
            break
        elif user_choice_2.upper() == "C":
            continue