from collections import deque


# Der Graph speichert Knoten und Kanten als gewichtete Adjazenzmatrix:
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

    def dfs(self, start):
        # Tiefensuche: Einen Nachbarn erst vollständig erkunden, bevor der
        # nächste Nachbar bearbeitet wird; die Rekursion bildet den Stack.
        visited = set()
        order = []

        # Alle Aufrufe von visit teilen sich in diesem Durchlauf dieselbe Menge visited und dieselbe Liste order.
        def visit(vertex):
            # Vor dem Weitergehen markieren: Eine Kante zurück darf keinen neuen Besuch starten.
            visited.add(vertex)
            order.append(vertex)
            source = self._index(vertex)

            # Wie in neighbours(): die Zeile des aktuellen Knotens lesen.
            for target, weight in enumerate(self.matrix[source]):
                neighbour = self.labels[target]
                if weight != 0 and neighbour not in visited:
                    visit(
                        neighbour
                    )  # Dieser Aufruf wird zuerst vollständig abgearbeitet.

        visit(start)
        return order

    def bfs(self, start):
        # Breitensuche: Knoten werden schichtweise besucht; die Queue hält
        # deshalb die bereits entdeckten, aber noch nicht bearbeiteten Knoten.
        visited = {start}  # Schon beim Einreihen als entdeckt markieren.
        queue = deque([start])
        order = []

        while queue:
            vertex = queue.popleft()  # Den am längsten wartenden Knoten bearbeiten.
            # Erst beim Herausnehmen aus der Queue kommt der Knoten in die Besuchsreihenfolge.
            order.append(vertex)
            source = self._index(vertex)

            for target, weight in enumerate(self.matrix[source]):
                neighbour = self.labels[target]
                if weight != 0 and neighbour not in visited:
                    # Sofort markieren: Andere Knoten dürfen ihn nicht erneut einreihen.
                    visited.add(neighbour)
                    queue.append(neighbour)

        return order


# roads = Graph(["A", "B", "C", "D"])
# roads.add_edge("A", "B", 4)
# roads.add_edge("A", "C", 2)
# roads.add_edge("B", "D", 3)
# roads.add_edge("C", "D", 1)
# print("Direct neighbours of A:", roads.neighbours("A"))
# roads.print_matrix()

# print("DFS from A:", roads.dfs("A"))
# print("BFS from A:", roads.bfs("A"))

one_way_roads = Graph(["A", "B", "C", "D"], directed=True)
one_way_roads.add_edge("A", "B", 4)
one_way_roads.add_edge("B", "D", 3)
one_way_roads.add_edge("C", "A", 2)
one_way_roads.add_edge("C", "D", 1)
one_way_roads.print_matrix()
# print("Directed DFS from A:", one_way_roads.dfs("A"))
# print("Directed BFS from A:", one_way_roads.bfs("A"))
print("Directed BFS from C:", one_way_roads.bfs("C"))
