class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Noch kein linkes Kind verknüpft.
        self.right = None  # Noch kein rechtes Kind verknüpft.
        self.height = 0  # Ein neuer Knoten ist "Leaf", also Blatt (d.h. ohne Kinder)


def in_order(node, visited):
    if node is None:
        return
    # In-order liefert die Werte eines Suchbaums von klein nach groß.
    in_order(node.left, visited)
    visited.append(node.value)
    in_order(node.right, visited)


class AVLTree:
    def __init__(self):
        self.root = None  # Der Baum beginnt ohne Wurzel.

    def _height(self, node):
        # None zählt als Höhe -1; so bekommt ein Blatt die Höhe 0.
        # Sonst die gespeicherte Höhe lesen, ohne den Teilbaum erneut zu durchlaufen.
        return -1 if node is None else node.height

    def _update_height(self, node):
        # Die Kinderhöhen müssen bereits aktuell sein.
        # Der längere Kinderweg plus eine Kante zum Kind ergibt die eigene Höhe.
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        # Rechts minus links: negativ = links höher, positiv = rechts höher.
        # Ausgeglichen ist der Knoten bei -1, 0 oder 1.
        return self._height(node.right) - self._height(node.left)

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
        self._update_height(
            node
        )  # Auf dem Rückweg: Die Kinderhöhen sind schon aktualisiert.
        # Auf dem Rückweg ausgleichen, nachdem das Kind fertig ist.
        # Der Aufrufer übernimmt die eventuell neue Teilbaumwurzel.
        return self._rebalance(node)

    def contains(self, target):
        return self._contains(self.root, target)

    def _contains(self, node, target):
        if node is None:
            return False  # Der passende Weg endet ohne Treffer.
        if target == node.value:
            return True
        if target < node.value:
            # Wegen der Suchbaumordnung muss nur links weitergesucht werden.
            return self._contains(node.left, target)
        # Ein größerer Wert kann nur im rechten Teilbaum liegen.
        return self._contains(node.right, target)

    def _find_min(self, node):
        current = node  # Hier wird ein nicht leerer Teilbaum übergeben.
        # Der kleinste Wert steht im äußersten linken Knoten.
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
        # Auf dem Rückweg ausgleichen, nachdem das Kind fertig ist.
        # Der Aufrufer übernimmt die eventuell neue Teilbaumwurzel.
        return self._rebalance(node)

    def _rotate_right(self, node):
        new_root = node.left  # Das linke Kind wird die neue Teilbaumwurzel.
        moved_subtree = (
            new_root.right
        )  # Inneren Teilbaum sichern, bevor sein Verweis überschrieben wird.
        new_root.right = node  # Die alte Wurzel wird rechtes Kind der neuen.
        # Werte zwischen new_root.value und node.value bleiben links von node.
        node.left = moved_subtree
        self._update_height(node)  # Erst die alte, nun tiefere Wurzel aktualisieren.
        self._update_height(
            new_root
        )  # Danach die neue Wurzel: Sie nutzt die aktualisierte Höhe von node.
        return new_root  # Der Aufrufer muss die neue Teilbaumwurzel wieder verknüpfen.

    def _rotate_left(self, node):
        new_root = node.right  # Das rechte Kind wird die neue Teilbaumwurzel.
        moved_subtree = (
            new_root.left
        )  # Inneren Teilbaum sichern, bevor sein Verweis überschrieben wird.
        new_root.left = node  # Die alte Wurzel wird linkes Kind der neuen.
        # Werte zwischen node.value und new_root.value bleiben rechts von node.
        node.right = moved_subtree
        self._update_height(node)  # Erst die alte, nun tiefere Wurzel aktualisieren.
        self._update_height(
            new_root
        )  # Danach die neue Wurzel: Sie nutzt die aktualisierte Höhe von node.
        return new_root  # Der Aufrufer muss die neue Teilbaumwurzel wieder verknüpfen.

    def _rebalance(self, node):
        # Nach der Änderung am Kind die eigene Höhe neu berechnen.
        self._update_height(node)
        balance = self._balance_factor(node)
        if balance < -1:  # Links zu hoch.
            if (
                self._balance_factor(node.left) > 0
            ):  # LR: Das linke Kind ist rechts höher.
                node.left = self._rotate_left(
                    node.left
                )  # Knick auflösen und neue Kindwurzel übernehmen.
            return self._rotate_right(node)  # LL oder zweiter Schritt von LR.
        if balance > 1:  # Rechts zu hoch.
            if (
                self._balance_factor(node.right) < 0
            ):  # RL: Das rechte Kind ist links höher.
                node.right = self._rotate_right(
                    node.right
                )  # Knick auflösen und neue Kindwurzel übernehmen.
            return self._rotate_left(node)  # RR oder zweiter Schritt von RL.
        return node  # Faktor -1, 0 oder 1: Diese Teilbaumwurzel bleibt erhalten.


avl = AVLTree()
# Diese Folge erzeugt zunächst eine Links-Links-Schieflage.
for value in [30, 20, 10]:
    avl.insert(value)
print(f"Root: {avl.root.value}")
print(f"Tree height: {avl.root.height}")
print(f"Root balance factor: {avl._balance_factor(avl.root)}")

# Zum Vergleich: Eine einzelne Rechtsrotation würde die gleiche Schieflage
# wie die automatische Ausgleichslogik im Beispiel beheben.
# avl.root = avl._rotate_right(avl.root)
# print(f"Root: {avl.root.value}")
# print(f"Tree height: {avl.root.height}")
# print(f"Root balance factor: {avl._balance_factor(avl.root)}")

for value in [25, 28]:
    # Nach jeder Einfügung werden Wurzel und Höhe zur Kontrolle ausgegeben.
    avl.insert(value)
    print(f"Inserted: {value}, root: {avl.root.value}, tree height: {avl.root.height}")

# Die In-order-Reihenfolge prüft, ob die Suchbaumordnung erhalten bleibt.
avl_values = []
in_order(avl.root, avl_values)
print(f"In-order: {avl_values}")


# Das Löschen testet zusätzlich die Ausgleichslogik nach einer Entfernung.
avl.delete(10)
after_delete = []
in_order(avl.root, after_delete)
print(f"After deleting 10 (in-order): {after_delete}")
print(f"Root: {avl.root.value}")
print(f"Tree height: {avl.root.height}")
print(f"Root balance factor: {avl._balance_factor(avl.root)}")
print(f"Contains 10: {avl.contains(10)}")
print(f"Contains 25: {avl.contains(25)}")
