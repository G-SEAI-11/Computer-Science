# Aufgabe 1: Eine Klasse für einzelne Bücher erstellen.
class Book:
    def __init__(self, name, author, release_date):
        # Die wichtigsten Eigenschaften des Buches speichern.
        self.name = name
        self.author = author
        self.release_date = release_date
        # Neue Bücher gelten zunächst als ungelesen.
        self.read = False

    def __str__(self):
        # Eine gut lesbare Darstellung des Buches zurückgeben.
        return f"'{self.name}', of {self.author} from {self.release_date}. and have I read it? ({"Jupp!"if self.read is True else "Nö!"})"


# Aufgabe 2: Eine Sammlung von Büchern verwalten.
class BookCollection:
    def __init__(self, books=None):
        # Ohne Übergabe wird eine leere Sammlung angelegt.
        if books is None:
            self.books = []
        else:
            # Die Sammlung darf nur aus einer Liste von Büchern bestehen.
            if not isinstance(books, list):
                raise TypeError("Books must be in a list")
            elif not all(isinstance(book, Book) for book in books):
                raise TypeError("All elements must be instance of book")
            self.books = books

    # Aufgabe 3: Ein neues Buch zur Sammlung hinzufügen.
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Ist kein Buch")

    # Andere gültige Version derselben Methode:
    # def add_book2(self, book):
    #     if not isinstance(book, Book):
    #      raise TypeError("Must be a Book instance")
    #     self.books.append(book)

    # Aufgabe 4: Ein Buch anhand seines Namens als gelesen markieren.
    # def mark_as_read(self, book_name):

    def mark_as_read(self, book_name):
        # Groß- und Kleinschreibung beim Suchen des Buches ignorieren.
        for book in self.books:
            if book.name.lower() == book_name.lower():
                book.read = True
                print(f"Das Buch {book_name} wurde gelesen.")
                return
            print(f"Das Buch {book_name} ist nicht da.")

    # def mark_as_read(self, book_name):
    #     for book in self.books:
    #         if book.name == book_name:
    #             book.read = True
    #             print("Buch ist gelesen")
    #             return
    #     print("Book not found.")

    # Aufgabe 5: Alle Bücher der Sammlung ausgeben.
    # def list_books(self):
    #     for book in self.books:
    #         print(book.name, book.author, book.release_date, book.read)

    def list_books(self):
        # Eine verständliche Meldung ausgeben, wenn die Sammlung leer ist.
        if not self.books:
            print("You don't own any books!\n")
            return
        # __str__ wird für jedes Buch automatisch aufgerufen.
        for book in self.books:
            print(book)


# Andere mögliche Version der Klasse: Jedes Buch über add_book hinzufügen.
# class BookCollection:
#     def __init__(self, books=None):
#         self.books = []

#         if books is not None:
#             for book in books:
#                 self.add_book(book)

# Beispielbücher erstellen.
book1 = Book("Beispielname", "Beispiel Author", 2000)
book2 = Book("Das Hobby", "Von Mir", 2026)
book3 = Book("Drittes Buch", "Dritte Autorin", 2020)

# Eigenschaften und die formatierte Darstellung eines Buches testen.
print(book1.name)
print("------")
print(book1)

# Eine Sammlung erstellen und ein weiteres Buch hinzufügen.
collection = BookCollection([book1, book2])
collection.add_book(book3)
print(len(collection.books))

# Ein Buch als gelesen markieren und den Status überprüfen.
(collection.mark_as_read("Beispielname"))
print(book1.read)

# Alle Bücher der Sammlung ausgeben.
collection.list_books()
# print(len(collection.books))

# Eine leere Sammlung testen.
empty_collection = BookCollection([])
# print(empty_collection.books)

# Ungültige Einträge würden beim Erstellen der Sammlung einen Fehler auslösen.
# invalid_collection = BookCollection([book1, "not a book"])
# print(invalid_collection)
empty_collection.list_books()
