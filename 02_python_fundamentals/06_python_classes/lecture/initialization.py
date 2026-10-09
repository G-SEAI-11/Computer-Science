# Methoden mit zwei Unterstrichen am Anfang und Ende heißen Dunder-Methoden.
# __init__ wird automatisch aufgerufen, sobald ein neues Counter-Objekt entsteht.
class Counter:
    def __init__(self, name, value=0):
        # self bezeichnet das gerade erzeugte Objekt.
        # Die übergebenen Werte werden als Attribute im Objekt gespeichert.
        self.name = name
        # Wird kein value angegeben, verwendet Python den Standardwert 0.
        self.value = value


# Ohne value wird der Standardwert aus __init__ verwendet.
first = Counter("A")
print(first.name)
# Hier wird zusätzlich ein eigener Startwert übergeben.
second = Counter("B", 10)
print(second.name)
# Der Name ist ein Pflichtargument und darf nicht fehlen.
# third = Counter()
# print(third.name)
print(first.name, first.value)
print(second.name, second.value)

# Die beiden Objekte wurden unabhängig voneinander initialisiert.
first.value = 5
print(first.value, second.value)
# Zu wenige oder zu viele Argumente führen zu einem TypeError.
# Counter()  # TypeError: not enough arguments
# Counter("C", 1, 2)  # TypeError: too many arguments

# Argumente können auch über ihre Parameternamen übergeben werden.
third = Counter(value=1, name="C")
print(third.name, third.value)
