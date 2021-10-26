class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f"Author: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Birthday: {self.birthday}\n" \
               f"Books: {self.books}\n\n"

    def __str__(self):
        return self.name + "|" + self.country + "|" + self.birthday + "_".join(self.books)


class Library:
    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def __repr__(self):
        books_str = " ".join(self.books)
        authors_str = " ".join(self.authors)
        return f'Library "{self.name}"\n' \
               f'Books: {books_str}\n' \
               f'Authors: {authors_str}\n\n'

    def __str__(self):
        return self.name + "|" + "_".join(self.books) + "|" + "_".join(self.authors)

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        if book.author not in self.authors:
            self.authors.append(book.author)
        return book

    def group_by_author(self, author: Author):
        result_list = []
        for book in self.books:
            if book.author == author:
                result_list.append(book)
        return result_list


class Book:
    book_count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.book_count += 1

    def __repr__(self):
        return f"Book: {self.name}\n" \
               f"Year: {self.year}\n" \
               f"Author: {self.author}\n\n"

    def __str__(self):
        return self.name + "|" + self.year + "|" + self.author



library1 = Library("Lib")
serega = Author("Sergey", "Ukraine", "1994")
library1.new_book("Booook", 1234, serega)
library1.new_book("ASDASDASD", 4567, serega)
print(library1.group_by_author(serega))
