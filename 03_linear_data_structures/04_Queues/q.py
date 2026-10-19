print("Queues")

# deque ("double-ended queue") aus der Standardbibliothek kann an beiden Enden in O(1) einfügen und entfernen
# from collections import deque


# Eine Queue (Warteschlange) arbeitet nach dem FIFO-Prinzip: "First In, First Out".
# Wer zuerst kommt, wird zuerst bedient – wie an der Eisdielenwarteschlange.
class Queue:
    def __init__(self) -> None:
        self.items = []

    # enqueue: stellt ein Element hinten an die Schlange an
    def enqueue(self, item):  # O(1)
        self.items.append(item)

    # dequeue: entfernt das vorderste Element und gibt es zurück
    def dequeue(self):  # O(n)

        # Designentscheidung: None statt Fehlermeldung zurückgeben
        if self.is_empty():
            return None

        # pop(0) ist O(n): Nach dem Entfernen vorne müssen alle übrigen Elemente einen Platz nach vorne rücken.
        return self.items.pop(0)

    # peek: schaut das vorderste Element an, ohne es zu entfernen
    def peek(self):  # O(1)
        return self.items[0]

    def is_empty(self):  # O(1)
        return len(self.items) == 0


warteschlange = Queue()

# Reihenfolge in der Schlange: Lennart, Wafaa, Ahmed
warteschlange.enqueue("Lennart")
warteschlange.enqueue("Wafaa")
warteschlange.enqueue("Ahmed")

# Die ersten drei Aufrufe entfernen Lennart, Wafaa und Ahmed – in genau der Reihenfolge, in der sie kamen (FIFO).
# Danach ist die Schlange leer und dequeue() gibt nur noch None zurück, statt abzustürzen.
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()
warteschlange.dequeue()


# Idee für ein schnelleres dequeue: Statt Elemente aus der Liste zu löschen,
# merken wir uns mit 'head' nur, wo die Schlange gerade vorne beginnt.
class DeQueue:
    def __init__(self) -> None:
        self.items = []
        # head zeigt auf den Index des aktuell vordersten Elements
        self.head = 0

    def enqueue(self, item):  # O(1)
        self.items.append(item)

    def dequeue(self):  #  O(1)

        if self.is_empty():
            return None

        # Ohne Aufräumen wächst die Liste immer weiter, weil alte Elemente nie gelöscht werden.
        # Idee: ab und zu nur den Teil ab head behalten.
        # if self.head > 100:
        # self.items = [...kopie ab head 100]

        # Kein Verschieben nötig: Wir lesen das Element bei head und rücken head eins weiter – O(1)
        dequeued_item = self.items[self.head]
        self.head += 1
        return dequeued_item

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
