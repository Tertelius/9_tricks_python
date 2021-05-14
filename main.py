import random as rnd

#  ------ 1. Выбор случайного элемента из последовательности элементов-----
#  функция random.choice(seq) позволяет выбрать случайный элемент из индексируемой последовательности. Речь идет о
#  списках, о кортежах и даже о строках.
#


my_list = [1, 2, 5, 8.4, 'go']
print(rnd.choice(my_list))
print(rnd.choice('привет_мир)'))

#  Практический пример:


def book_picker(books):
    book_choice = rnd.choice(books)
    books.remove(book_choice)
    return f"You picked '{book_choice}'"

books = ["Harry potter", "Don Quixote", "Learn Python by Daniel Diaz", "Dracula"]
print(book_picker(books))
print(books)


#  ----- 2.




