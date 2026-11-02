# Die Reihenfolge der Labels legt fest, welche Zeile und Spalte zu einem Knoten gehört.
label = ["A", "B", "C", "D"]

# Die Matrix speichert die Verbindungen zwischen den Knoten:
# Zeile = Startknoten, Spalte = Zielknoten, 0 = keine Kante.
matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

# Direkter Zugriff auf einen Matrixeintrag:
# Der Eintrag in Zeile A und Spalte C zeigt, ob A mit C verbunden ist.
print("A -> C:", matrix[0][2])
print("C -> A:", matrix[2][0])
print("A -> D:", matrix[0][3])


def has_edge(label_from, label_to):
    """Prüft, ob zwischen zwei Knoten eine Kante gespeichert ist."""
    row = label.index(label_from)
    column = label.index(label_to)
    return matrix[row][column] != 0


# Mit den Labels lässt sich die passende Zeile und Spalte lesbarer auswählen.
print("A -> C:", has_edge("A", "C"))
print("A -> D:", has_edge("A", "D"))
