from collections import deque

preorder = [8, 5, 1, 7, 10, 12]
next_value = preorder[3]  # 8, 5 und 1 wurden bereits gelesen.
# Links von 1 sind nur kleinere Werte erlaubt; eine endliche Untergrenze fehlt.
print("Left of 1:", float("-inf") < next_value < 1)
# Rechts von 1 gilt zusätzlich weiterhin die Obergrenze des Vorfahren 5.
print("Right of 1, below 5:", 1 < next_value < 5)
# Rechts von 5 muss der Wert größer als 5, aber weiterhin kleiner als 8 sein.
print("Right of 5, below 8:", 5 < next_value < 8)


class BinaryNode:
    def __init__(self, value):
        self.value = value
        # Die Kindverbindungen entstehen erst beim rekursiven Aufbau.
        self.left = None
        self.right = None


def bst_from_preorder(preorder):
    def build(lower_bound, upper_bound, index):
        # Alle Werte sind verbraucht: Dieser Kindplatz bleibt leer.
        if index == len(preorder):
            return None, index
        value = preorder[index]
        # Nur Werte innerhalb beider Grenzen gehören in diesen Teilbaum.
        if value <= lower_bound or value >= upper_bound:
            # Nicht verbrauchen: Ein wartender Aufruf kann diesen Wert noch brauchen.
            return None, index

        index += 1  # Erst jetzt ist der Wert einem Knoten zugeordnet.
        node = BinaryNode(value)
        # Links: Untergrenze erben, eigenen Wert als neue Obergrenze setzen.
        node.left, index = build(lower_bound, value, index)
        # Rechts: eigenen Wert als Untergrenze setzen, Obergrenze erben.
        # Der zurückgegebene Index überspringt die bereits links verbrauchten Werte.
        node.right, index = build(value, upper_bound, index)
        return (
            node,
            index,
        )  # Teilbaum und Leseposition an den wartenden Aufruf zurückgeben.

    # An der Wurzel sind beide Grenzen offen: negative und positive Unendlichkeit.
    # _ nimmt den letzten Index auf; nach dem Aufbau brauchen wir nur die Wurzel.
    root, _ = build(float("-inf"), float("inf"), 0)
    return root


root = bst_from_preorder(preorder)
print("Root:", root.value)
print("Right child of 5:", root.left.right.value)


def tree_to_list_level_order(root):
    # Ohne Wurzel gibt es keine Knoten anzuzeigen.
    if root is None:
        return []

    result = []
    queue = deque([root])  # Zu Beginn wartet nur die Wurzel.

    while queue:
        node = queue.popleft()  # Den am längsten wartenden Eintrag verarbeiten.
        if node is None:
            # Die Lücke festhalten, aber für einen leeren Platz keine Kinder anstellen.
            result.append(None)
        else:
            result.append(node.value)
            # Links vor rechts anstellen, einschließlich fehlender Kinder.
            queue.append(node.left)
            queue.append(node.right)

    # Nur Lücken am Ende entfernen; innere Lücken zeigen die Baumform.
    # result prüft zuerst, ob die Liste noch Einträge für den Zugriff [-1] enthält.
    while result and result[-1] is None:
        result.pop()

    return result


print(tree_to_list_level_order(root))

second_root = bst_from_preorder([1, 3])
print(tree_to_list_level_order(second_root))
