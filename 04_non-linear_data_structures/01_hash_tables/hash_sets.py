# Ein HashSet speichert jeden Schlüssel höchstens einmal.
class HashSet:
    def __init__(self):
        # Jeder Schlüssel wird in einem von vier Buckets abgelegt.
        self.buckets = [[] for _ in range(4)]

    # Der Hashwert bestimmt, in welchem Bucket ein Schlüssel gesucht wird.
    # Der Unterstrich kennzeichnet die Methode als interne Hilfsmethode.
    def _index(self, key):
        return hash(key) % len(self.buckets)

    def add(self, key):
        # Ein Schlüssel wird nur eingefügt, wenn er noch nicht vorhanden ist.
        bucket = self.buckets[self._index(key)]
        if key not in bucket:
            bucket.append(key)

    def contains(self, key):
        # Prüfe, ob der Schlüssel im passenden Bucket vorhanden ist.
        bucket = self.buckets[self._index(key)]
        return key in bucket

    def remove(self, key):
        # Entferne den Schlüssel, falls er im passenden Bucket vorhanden ist.
        bucket = self.buckets[self._index(key)]
        if key in bucket:
            bucket.remove(key)


# Beispiel für das Hinzufügen, Suchen und Löschen von Schlüsseln.
demo_set = HashSet()
demo_set.add(10)
demo_set.add(14)
demo_set.add(10)
print(demo_set.buckets)
print(demo_set.contains(14))
demo_set.remove(10)
print(demo_set.buckets)


# numbers = {"One", "Two","Three"}
