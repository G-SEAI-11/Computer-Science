class Graph:
    def __init__(self, labels, directed=False):
        # Eigene Namensliste: Änderungen an der übergebenen Liste wirken hier nicht mit.
        self.labels = labels.copy()
        self.directed = directed  # False: beide Richtungen; True: nur Start → Ziel.
        self.matrix = []
        for (
            _
        ) in labels:  # Ein Durchlauf pro Knoten; den Namen selbst brauchen wir nicht.
            # Jede Zeile ist eine eigene Liste: Eine Zelle darf nicht mehrere Zeilen ändern.
            self.matrix.append(
                [0] * len(labels)
            )  # Eine 0 pro Zielknoten: noch keine Kante.

    def _index(self, label):
        # Zum Beispiel: "C" → 2. Ein unbekannter Name löst hier einen ValueError aus.
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        # Diese Demo nutzt positive Entfernungen; 0 bedeutet keine Kante.
        if weight <= 0:
            # Den Aufruf abbrechen, bevor eine Matrixzelle verändert wird.
            raise ValueError("weight must be positive")

        # Knotennamen in die Zeilen- und Spaltenindizes der Matrix übersetzen.
        source = self._index(label_from)
        target = self._index(label_to)
        self.matrix[source][target] = weight  # Zeile = Start, Spalte = Ziel.

        # Nur bei directed=False: dieselbe Kante auch von Ziel nach Start eintragen.
        if not self.directed:
            self.matrix[target][source] = weight

    def remove_edge(self, label_from, label_to):
        # Knotennamen in die Zeilen- und Spaltenindizes der Matrix übersetzen.
        source = self._index(label_from)
        target = self._index(label_to)
        # 0 entfernt nur die Verbindung; beide Knoten bleiben im Graphen.
        self.matrix[source][target] = 0
        if not self.directed:
            # Ungerichtet gehört die Gegenrichtung zur selben Kante und muss auch weg.
            self.matrix[target][source] = 0

    def neighbours(self, label):
        # Nur die Zeile des Startknotens lesen: Sie enthält dessen ausgehende Kanten.
        row = self.matrix[self._index(label)]
        result = []
        # index ist die Zielspalte; weight ist das dort gespeicherte Gewicht.
        for index, weight in enumerate(row):
            # Nur direkte Kanten liefern einen Nachbarn; 0 wird übersprungen.
            if weight != 0:
                result.append(
                    self.labels[index]
                )  # Den Zielnamen sammeln, nicht das Gewicht.
        # Erst nach allen Spalten die vollständige Nachbarliste zurückgeben.
        return result

    def print_matrix(self):
        # * übergibt die Listeneinträge einzeln an print.
        # Die freie erste Spalte lässt Platz für die Zeilennamen darunter.
        print(" ", *self.labels)
        # enumerate liefert den Zeilenindex und die zugehörige Zeile zusammen.
        for index, row in enumerate(self.matrix):
            print(
                self.labels[index], *row
            )  # Derselbe Index liefert den passenden Knotennamen.


roads = Graph(["A", "B", "C", "D"])
print("Empty graph:")
roads.print_matrix()

roads.add_edge("A", "B", 4)
print("After adding A-B:")
roads.print_matrix()

roads.add_edge("A", "C", 2)
roads.add_edge("B", "D", 3)
roads.add_edge("C", "D", 1)
print("All roads:")
roads.print_matrix()

print("Neighbours of A:", roads.neighbours("A"))
print("Neighbours of C:", roads.neighbours("C"))

roads.remove_edge("C", "D")
print("After removing C-D:")
roads.print_matrix()
print("Neighbours of C:", roads.neighbours("C"))

# Ein neues Objekt mit eigener Matrix; der bisherige Graph roads bleibt erhalten.
one_way_roads = Graph(["A", "B", "C", "D"], directed=True)
one_way_roads.add_edge("A", "B", 4)
print("One-way road A -> B:")
one_way_roads.print_matrix()
print("Neighbours of A:", one_way_roads.neighbours("A"))
print("Neighbours of B:", one_way_roads.neighbours("B"))
