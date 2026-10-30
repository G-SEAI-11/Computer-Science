class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Noch kein linkes Kind verknüpft.
        self.right = None  # Noch kein rechtes Kind verknüpft.


def in_order(node, visited):
    if node is None:
        return
    in_order(node.left, visited)
    visited.append(node.value)
    in_order(node.right, visited)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Das Einfügen beginnt bei der Wurzel des Baums.
        # Der Rückgabewert kann eine neue Wurzel sein, wenn der Baum leer war.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            # Eine leere Stelle ist die richtige Position für den neuen Wert.
            return BinaryNode(value)
        if value < node.value:
            # Kleinere Werte gehören in den linken Teilbaum.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Größere Werte gehören in den rechten Teilbaum.
            node.right = self._insert_recursive(node.right, value)
        # Bei gleichen Werten wird nichts eingefügt: Duplikate werden ignoriert.
        return node

    def contains(self, target):
        return self._contains(self.root, target)

    def _contains(self, node, target):
        if node is None:
            return False  # Der passende Weg endet ohne Treffer.
        if target == node.value:
            return True
        if target < node.value:
            return self._contains(node.left, target)
        return self._contains(node.right, target)

    def _find_min(self, node):
        current = node  # Hier wird ein nicht leerer Teilbaum übergeben.
        while current.left is not None:
            current = current.left
        return current

    def delete(self, target):
        self.root = self._delete(
            self.root, target
        )  # Auch eine entfernte Wurzel (Root) übernehmen.

    def _delete(self, node, target):
        if node is None:
            return None  # Nicht gefunden: Hier bleibt der Teilbaum leer.
        if target < node.value:
            node.left = self._delete(node.left, target)
        elif target > node.value:
            node.right = self._delete(node.right, target)
        else:
            if node.left is None and node.right is None:
                return None  # Blatt: Der Elternverweis wird None.
            if node.left is None:
                return node.right  # Das rechte Kind übernimmt den Platz.
            if node.right is None:
                return node.left  # Das linke Kind übernimmt den Platz.
            successor = self._find_min(node.right)  # Ersatzwert bestimmen
            node.value = (
                successor.value
            )  # Nur den Wert übernehmen; beide Verbindungen (zu den Kindern) bleiben.
            node.right = self._delete(
                node.right, successor.value
            )  # Doppelten Ersatzwert löschen
        return node


tree = BinarySearchTree()
for value in [8, 5, 10, 1, 7, 12]:
    tree.insert(value)

built_values = []
in_order(tree.root, built_values)
print(built_values)

print(tree.contains(7))
print(tree.contains(9))

print(tree._find_min(tree.root).value)
print(tree._find_min(tree.root.right).value)

tree.delete(1)
after_leaf = []
in_order(tree.root, after_leaf)
print(after_leaf)

tree.delete(10)
after_one_child = []
in_order(tree.root, after_one_child)
print(after_one_child)

tree.delete(8)
after_two_children = []
in_order(tree.root, after_two_children)
print(after_two_children)
