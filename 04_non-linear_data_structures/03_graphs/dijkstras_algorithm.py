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


graph = Graph(["A", "B", "C", "D", "E", "F"])
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "C", 11)
graph.add_edge("B", "D", 9)
graph.add_edge("B", "E", 7)
graph.add_edge("C", "E", 3)
graph.add_edge("D", "E", 13)
graph.add_edge("D", "F", 2)
graph.add_edge("E", "F", 6)
graph.print_matrix()


def closest_unvisited(distances, visited):
    closest = None  # Noch kein erreichbarer, unbesuchter Knoten gefunden.
    smallest_distance = float("inf")
    for vertex in distances:
        if vertex not in visited and distances[vertex] < smallest_distance:
            closest = vertex
            smallest_distance = distances[
                vertex
            ]  # Neuer Vergleichswert für den Rest der Suche.
    return closest


# Zustand nach der Bearbeitung von B aus der Grafik.
# sample_distances = {"A": 0, "B": 4, "C": 5, "D": 13, "E": 11, "F": float("inf")}
# sample_visited = {"A", "B"}
# print("Next vertex:", closest_unvisited(sample_distances, sample_visited))


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph.labels}
    previous = {vertex: None for vertex in graph.labels}
    distances[start] = 0
    visited = set()

    for _ in graph.labels:  # Höchstens einmal pro Knoten einen neuen Knoten bearbeiten.
        vertex = closest_unvisited(distances, visited)
        if vertex is None:
            break  # Alle übrigen Knoten sind schon besucht oder unerreichbar.

        source = graph.labels.index(
            vertex
        )  # Den Namen in die passende Matrixzeile übersetzen.
        for target, weight in enumerate(graph.matrix[source]):
            neighbour = graph.labels[target]
            if weight == 0 or neighbour in visited:
                continue  # Keine Kante oder bereits endgültige Distanz: überspringen.
            candidate = distances[vertex] + weight
            if candidate < distances[neighbour]:
                distances[neighbour] = candidate
                previous[neighbour] = (
                    vertex  # Über diesen Knoten ist der Weg günstiger.
                )
        visited.add(vertex)  # Erst nach der ganzen Zeile ist dieser Knoten fertig.
    return distances, previous


distances, previous = dijkstra(graph, "A")
print("Costs from A:", distances)
print("Previous:", previous)
