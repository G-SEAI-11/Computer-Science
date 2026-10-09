# Listen sind bereits fertige Objekte einer eingebauten Python-Klasse.
numbers = [1, 2, 3]
# Methoden verändern ein Objekt oder liefern Informationen darüber.
numbers.append(4)
print(numbers)
# Mit type() lässt sich die Klasse eines Objekts anzeigen.
print(type(numbers))
print(type("Hello"))  # noqa: UP003


# Eine eigene Klasse beschreibt, welche Art von Objekten wir erzeugen möchten.
class Counter:
    # pass bedeutet: Die Klasse hat vorerst keinen eigenen Inhalt.
    pass


# Durch einen Aufruf der Klasse wird ein neues Objekt (eine Instanz) erzeugt.
first = Counter()
second = Counter()
print(type(first))
# Zwei getrennte Aufrufe erzeugen zwei verschiedene Objekte.
print(first is second)

# Attribute speichern Daten direkt in einem Objekt.
# Jedes Objekt der Klasse Counter besitzt seinen eigenen Zustand.
first.name = "A"
first.value = 2
second.name = "B"
second.value = 10
print(first.name, first.value)
print(second.name, second.value)

first.value += 1
print(first.value, second.value)
# Ohne eigene __str__-Methode zeigt print() die Standarddarstellung des Objekts.
print(first)

# isinstance() prüft, ob ein Objekt zu einer bestimmten Klasse gehört.
print(isinstance(first, Counter))
print(isinstance("A", Counter))
