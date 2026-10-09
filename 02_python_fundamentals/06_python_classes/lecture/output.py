class Counter:
    def __init__(self, name, value=0):
        # __init__ speichert beim Erzeugen die Werte im neuen Objekt.
        self.name = name
        # Ohne value wird der Standardwert 0 verwendet.
        self.value = value

    def __str__(self):
        # Diese Darstellung wird von print() automatisch verwendet.
        return f"{self.name}: {self.value}"


# print() nutzt die __str__-Methode des Counter-Objekts.
first = Counter("A")
print(first)
# str() erwartet ein Objekt und ruft ebenfalls dessen __str__-Methode auf.
text = str(Counter)
print(text)
