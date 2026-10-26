# Eine HashMap speichert zu jedem Schlüssel einen Wert.
class HashMap:
    def __init__(self):
        # Jeder Eintrag wird in einem von vier Buckets abgelegt.
        self.buckets = [[] for _ in range(4)]

    # Der Hashwert bestimmt, in welchem Bucket ein Schlüssel gesucht wird.
    # Der Unterstrich kennzeichnet die Methode als interne Hilfsmethode.
    def _index(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        # Bei einem bereits vorhandenen Schlüssel wird nur der Wert aktualisiert.
        bucket = self.buckets[self._index(key)]
        for index, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return
        # Mehrere Schlüssel im gleichen Bucket werden als Liste gespeichert.
        bucket.append((key, value))

    def get(self, key):
        # Suche den Schlüssel im berechneten Bucket und gib seinen Wert zurück.
        bucket = self.buckets[self._index(key)]
        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value
        return None  # nur wenn nach allen Vergleichen der Schlüssel fehlt

    def contains(self, key):
        # Prüfe, ob der Schlüssel im passenden Bucket vorhanden ist.
        bucket = self.buckets[self._index(key)]
        for stored_key, stored_value in bucket:
            if stored_key == key:
                return True
        return False

    def remove(self, key):
        # Entferne den Eintrag mit dem Schlüssel aus dem passenden Bucket.
        bucket = self.buckets[self._index(key)]
        for index, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                del bucket[index]
                return


# Beispiel für das Speichern, Aktualisieren, Suchen und Löschen von Einträgen.
my_map = HashMap()
my_map.put("Book", 12.99)
my_map.put("Laptop", 999.00)
print(my_map.buckets)
my_map.put("Laptop", 900.00)
print(my_map.buckets)
print("Book price:", my_map.get("Book"))
print("Contains 'Phone'?", my_map.contains("Phone"))
my_map.remove("Book")
print(my_map.buckets)
