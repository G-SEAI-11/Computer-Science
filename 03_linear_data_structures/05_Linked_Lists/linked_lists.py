# Eine Node (Knoten) ist ein einzelnes Glied der Kette: Sie speichert einen Wert
# und einen Pointer ('next') auf die nächste Node. None bedeutet: Hier endet die Kette.
# Anders als bei einer Python-Liste liegen die Elemente nicht nebeneinander im Speicher –
# jede Node weiß nur, wo ihr Nachfolger ist.
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


# Die LinkedList selbst kennt nur die erste Node ('head').
# Alle anderen Nodes erreichen wir nur, indem wir uns von head aus über die next-Pointer weiterhangeln.
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.tail = None # Wir können die Klasse noch erweitern. Nichts spricht dagegen, auch eine Referenz auf die letzte Node zu halten.

    # append: hängt eine neue Node ans Ende der Kette
    def append(self, value):  # O(n)
        new_node = Node(value)

        # Die Liste ist leer: die neue Node wird zum head
        if not self.head:
            self.head = new_node
        else:
            # Traversal: Wir starten bei head und folgen den next-Pointern,
            # bis wir bei der letzten Node angelangt sind (wo next None ist).
            # Deshalb O(n) – wir müssen einmal durch die ganze Kette laufen.
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            # Die bisher letzte Node zeigt jetzt auf die neuen
            current_node.next = new_node

    # prepend: setzt eine neue Node an den Anfang – O(1), denn kein Traversal nötig.
    # Neue Node zeigt auf den alten head und wird selbst zum neuen head.
    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    # pop: entfernt den letzten Knoten und gibt seinen Wert zurück
    def pop(self):  # O(n)
        # Leere Liste: nichts zu entfernen
        if not self.head:
            return None

        # Nur eine Node: Kopf entfernen
        if not self.head.next:
            val = self.head.value
            self.head = None
            return val

        # Wir brauchen zwei Pointer: Die letzte Node wollen wir entfernen,
        # aber ändern müssen wir die vorletzte ('prev_node') – next muss dort auf None gesetzt werden.
        current_node = self.head
        prev_node = self.head

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        # Die letzte Node "abschneiden": Ohne Pointer auf ist sie nicht mehr Teil der Kette. Der Garbage Collector in Python kümmert sich
        # automatisch um das unverbundene Objekt und löscht es.
        val = current_node.value
        prev_node.next = None
        return val

    # def remove(self, value):
    #     pass

    # def remove(self, value):
    #     #############################################
    #     if not self.head:
    #         return None

    #     prev_node = self.head
    #     found_node = prev_node.next

    #     while prev_node is not None and prev_node.next != value:
    #         prev_node = found_node
    #         if prev_node is not None and prev_node.next == value:
    #             found_node = prev_node.next
    #             prev_node.next = found_node.next

    #             val = found_node.value
    #             found_node.next = None

    #             return val
    #     return None

    # def remove_by_value(self, value):
    #     if self.head == None:
    #         return "Nothing to remove"
    #     aktueller_knoten = self.head
    #     letzter_knoten = None
    #     while aktueller_knoten:

    #         if (
    #             aktueller_knoten.value == value and aktueller_knoten is self.head
    #         ):  # wenn es der erste Knoten ist, dann wird der einfach ausgehängt
    #             self.head = aktueller_knoten.next
    #             break

    #         elif aktueller_knoten.value == value:
    #             letzter_knoten.next = aktueller_knoten.next
    #             print(
    #                 f"{letzter_knoten.value} mit {aktueller_knoten.next.value if aktueller_knoten.next else "Nichts"} verbunden"
    #             )
    #             aktueller_knoten = aktueller_knoten.next

    #         else:
    #             letzter_knoten = aktueller_knoten
    #             aktueller_knoten = aktueller_knoten.next

    # __str__ bestimmt, was print() ausgibt.
    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(f"[{ curr.value }]")
            curr = curr.next

        return " -> ".join(nodes) + " -> None"


my_linked_list = LinkedList()

# Eine LinkedList kann – wie eine Python-Liste – Werte beliebigen Typs speichern
my_linked_list.append(42)
my_linked_list.append("test")
my_linked_list.append(False)
my_linked_list.append(123)
my_linked_list.append(1.23)

print(my_linked_list)
my_linked_list.remove_by_value("test")
print(my_linked_list)


last = my_linked_list.pop()
print(my_linked_list)
print(last)


# my_py_list = []

# my_py_list.append(42)

# [1, 2, 3] + [6, 7, 8]

# 42.plus(52)


# 42 + 54

# "Guten, " + "morgen"
