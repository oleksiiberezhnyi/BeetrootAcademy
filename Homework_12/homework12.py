# Task 1


class Animal:

    def talk(self):
        return ":-)"


class Dog(Animal):

    def talk(self):
        return "Woof! Woof!"


class Cat(Animal):

    def talk(self):
        return "Meeooow!"


def animal_say(animal):
    print(animal.talk())


animal_say(Dog())
animal_say(Cat())


# Task 2


class Author:

    def __init__(self, author_name, country, birthday):
        self.author_name = author_name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f'"{self.author_name}, {self.country}, {self.birthday}"'

    def __str__(self):
        return str(f'"{self.author_name}, {self.country}, {self.birthday}"')


class Book:
    COUNT_OF_ALL_BOOK = 0

    def __init__(self, book_name, year, author: Author):
        self.book_name = book_name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'"book name: {self.book_name};' \
               f'year: {self.year};' \
               f'author: {self.author}"'

    def __str__(self):
        return str(f'"book name: {self.book_name};'
                   f'year: {self.year};'
                   f'author: {self.author}"')


class Library:

    def __init__(self, library_name: str = "Library"):
        self.library_name = library_name
        self.books = []
        self.authors = []
        self._books_by_author = []
        self._books_by_year = []

    def new_book(self, book_name: str, year: int, author: Author):
        self.books.append({"name": book_name, "year": year, "author": author})
        self.authors.append(author)
        Book.COUNT_OF_ALL_BOOK += 1
        return Book(book_name, year, author)

    def group_by_author(self, author: Author):
        for nested_dict in self.books:
            if nested_dict["author"] == author:
                # .__dict__ because TypeError:
                # 'Author' object is not subscriptable
                self._books_by_author.append(
                    {author.__dict__["author_name"]: nested_dict["name"]}
                )
        return self._books_by_author

    def group_by_year(self, year: int):
        for nested_dict in self.books:
            if nested_dict["year"] == year:
                self._books_by_year.append(
                    {nested_dict["name"]: nested_dict["year"]}
                )
        return self._books_by_year

    def __repr__(self):
        return f'{self.library_name}\n' \
               f'Books: {self.books}\n' \
               f'Authors: {list(dict.fromkeys(self.authors))}'

    def __str__(self):
        return str(f'{self.library_name}\n'
                   f'Books: {self.books}\n'
                   f'Authors: {list(dict.fromkeys(self.authors))}')


author1 = Author("Stephen King", "USA", "21.09.1947")
author2 = Author("J.R.R. Tolkien", "South Africa", "03.01.1892")
lib = Library()
lib.new_book("The Outsider", 2018, author1)
lib.new_book("Elevation", 2018, author1)
lib.new_book("The Institute", 2019, author1)
lib.new_book("The Hobbit", 1937, author2)
lib.new_book("The Lord of the Rings", 1967, author2)
print(lib.books)
print(lib.group_by_author(author2))
print(lib.group_by_year(2018))
print(lib)
print(Book.COUNT_OF_ALL_BOOK)


# Task 3


class Fraction:

    def __init__(self, fraction):
        self.fraction = fraction
        if isinstance(self.fraction, str):
            raise Exception("Need to pass a number")

    def __add__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        return round(self.fraction + other.__dict__["fraction"], 3)

    def __sub__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        return round(self.fraction - other.__dict__["fraction"], 3)

    def __mul__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        return round(self.fraction * other.__dict__["fraction"], 3)

    def __truediv__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        try:
            return round(self.fraction / other.__dict__["fraction"], 3)
        except ZeroDivisionError:
            return "Infinitely large number"


x = Fraction(4 / 5)
y = Fraction(3 / 8)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
