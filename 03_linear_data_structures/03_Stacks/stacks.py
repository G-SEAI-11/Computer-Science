print("Stapel")


# Eine normale Python-Liste kann schon als Stack dienen:
# append() legt oben drauf, pop() nimmt das oberste Element wieder weg.
# myStack = []

# myStack.append("Erste Element")
# myStack.append("Zweites Element")

# lastEl = myStack.pop()


# Ein Stack (Stapel) arbeitet nach dem LIFO-Prinzip: "Last In, First Out".
# Was zuletzt hineingelegt wurde, kommt als Erstes wieder heraus – wie bei einem Tellerstapel.
class Stack:
    def __init__(self) -> None:
        # Intern speichern wir die Elemente in einer Liste; das Ende der Liste ist die "Oberseite" des Stapels.
        self.items = []
        self.min = None # Eigene Datenstrukturen können um weitere Attribute ergänzt werden, z.B. wenn ein Stack immer schnell den kleinsten Wert ausgeben soll.

    # push: legt ein Element oben auf den Stapel – O(1)
    def push(self, item):
        self.items.append(item)

    # pop: entfernt das oberste Element und gibt es zurück – O(1)
    def pop(self):
        return self.items.pop()

    # peek: schaut das oberste Element nur an, ohne es zu entfernen - O(1)
    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


myStack = Stack()

# Stapel nach den drei push-Aufrufen (oben = rechts): [1, 2, 3]
myStack.push(1)
myStack.push(2)
myStack.push(3)

# pop() holt die 3, weil sie zuletzt hinzugefügt wurde (LIFO)
lastItem = myStack.pop()

print(lastItem)  # 3

# Jetzt liegt die 2 oben – peek() zeigt sie, lässt sie aber auf dem Stapel
print(myStack.peek())  # 2


# Praxisbeispiel: Der "Zurück"-Button im Browser ist ein Stack.
# Jede besuchte Seite wird gepusht, "Zurück" macht ein pop auf die zuletzt besuchte Seite.
# browser_history = Stack()

# browser_history.push("wikipedia.de")
# browser_history.push("wikipedia.de/pythos")
# browser_history.push("wikipedia.de/Guido-van-Rossum")
# browser_history.push("wikipedia.de/dropbox")

# browser_history.pop()


# Rekursion nutzt intern ebenfalls einen Stack: den Call Stack.
# Jeder Aufruf von fakultät() wird auf den Call Stack gelegt und wartet,
# bis der innere Aufruf fertig ist. Dann werden sie in umgekehrter Reihenfolge abgearbeitet.
def fakultät(n):
    # Abbruchbedingung (Base Case): wie die Endbedingung in einer while-Schleife
    if n <= 1:
        return 1

    return n * fakultät(n - 1)


# 5 * 4 * 3 * 2 * 1

print(fakultät(3))  # 6


# Dieselbe Berechnung ohne Rekursion. Wir bauen den Call Stack selbst mit unserer Stack-Klasse nach.
def fakulät_iterativ(n):
    stack = Stack()

    # Phase 1: alle Zahlen von n bis 2 auf den Stapel legen (wie die wartenden rekursiven Aufrufe)
    while n > 1:
        stack.push(n)
        n -= 1

    result = 1

    # Phase 2: Zahlen wieder vom Stapel nehmen und aufmultiplizieren (wie die Rückgabe der Aufrufe)
    while not stack.is_empty():
        result *= stack.pop()

    return result


print(fakulät_iterativ(5))  # 120
