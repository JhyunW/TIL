# book.py
number_of_book = 100

def decrease_book(x):
    global number_of_book
    number_of_book -= x
    print("남은 책의 수 :", number_of_book)
    return number_of_book