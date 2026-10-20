class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


# Eine Queue (FIFO), gebaut aus einer LinkedList.
# Der Trick: Wir merken uns nicht nur den Anfang ('head'), sondern auch das Ende ('tail').
# So können wir hinten anfügen und vorne entfernen, ohne jemals durch die Kette laufen zu müssen.
# Zum Vergleich: Die Queue mit Python-Liste in 04_Queues brauchte für dequeue O(n), oder einen Zeiger und gelegentliches Umkopieren.
class QueueLL:
    def __init__(self):
        self.head = None  # vorderstes Element
        self.tail = None  # letztes Element
        self.length = 0

    # enqueue: stellt eine neue Node hinten an – O(1), denn tail zeigt direkt aufs Ende
    def enqueue(self, value):
        new_node = Node(value)

        # Leere Queue: Der neue Node ist gleichzeitig erster und letzter
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # Die bisher letzte Node zeigt auf die neue, dann rückt tail weiter
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    # dequeue: entfernt den vordersten Knoten und gibt seinen Wert zurück
    def dequeue(self):  # O(1)
        if not self.head:
            return None

        # head rückt einfach eine Node weiter – der alte vorderste Knoten ist damit nicht mehr Teil der Kette
        dequeued_val = self.head.value
        self.head = self.head.next

        # War das die letzte Node, ist die Queue jetzt leer – dann muss auch tail gelöscht werden
        if not self.head:
            self.tail = None

        self.length -= 1
        return dequeued_val

    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(f"[{curr.value}]")
            curr = curr.next
        return "(Head) " + " <- ".join(nodes) + " (Tail)"
