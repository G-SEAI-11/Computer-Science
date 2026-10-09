class Counter:
    def __init__(self, name, value=0):
        # __init__ legt den Anfangszustand jedes neuen Objekts fest.
        self.name = name
        self.value = value

    def __str__(self):
        # __str__ bestimmt die lesbare Darstellung für print() und str().
        return f"{self.name}: {self.value}"

    def add(self, amount):
        # Eine Methode kann den Zustand des Objekts verändern.
        if amount < 0:
            # Ungültige Werte werden mit einer passenden Ausnahme abgelehnt.
            raise ValueError("amount must not be negative")
        self.value += amount

    def reset(self):
        # Diese Methode setzt den Zähler wieder auf seinen Anfangswert zurück.
        self.value = 0


# Ein Objekt wird erzeugt und anschließend über seine Methoden verwendet.
counter = Counter("A", 2)
print(counter)
counter.add(10)
print(counter)
counter.reset()
print(counter)
# Der Fehler wird abgefangen, damit das Programm danach weiterlaufen kann.
try:
    counter.add(-1)
except ValueError as error:
    print(error)
print(counter)
