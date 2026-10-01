# Das Modul copy stellt deepcopy() zum Kopieren verschachtelter Listen bereit.
import copy

# Listen sind veränderbar, behalten die Reihenfolge und erlauben Duplikate.
fruits = ["apple", "banana", "cherry", "apple", "mango"]
print(fruits)
# len() zählt die Elemente der Liste, einschließlich Duplikaten.
# print(len(fruits))

# Slicing: [start:end] liefert eine neue Liste; end ist nicht enthalten.
# Indizes beginnen bei 0: [3:4] liefert hier ["apple"], nicht den String "apple".
print(fruits[3:4])

# in prüft, ob ein Wert in der Liste vorkommt, und liefert True oder False.
print("apple" in fruits)

# Elemente einfügen: Diese Methoden verändern die bestehende Liste.
fruits.append("orange")  # Hängt ein einzelnes Element am Ende an.
fruits.insert(1, "grape")  # Fügt vor Index 1 ein; folgende Elemente rücken weiter.
fruits.extend(["peach", "melon"])  # Hängt die Elemente der anderen Liste einzeln an.
print(fruits)

# Elemente entfernen
fruits.remove("apple")  # Entfernt nur das erste Vorkommen dieses Werts.
print(fruits)
fruits.pop()  # Entfernt das letzte Element und gibt es zurück.
fruits.pop(1)  # Entfernt das Element am aktuellen Index 1 und gibt es zurück.
print(fruits)

# Elemente ersetzen: Zuweisungen verändern die bestehende Liste.
fruits[0] = "watermelon"
# Ersetzt die Elemente an Index 1 und 2; die obere Grenze 3 ist ausgeschlossen.
fruits[1:3] = ["kiwi", "lemon"]
print(fruits)

# Weitere Beispiele zum Aktivieren und Ausprobieren
# Ein Slice liest einen Ausschnitt aus, ohne die ursprüngliche Liste zu verändern.
# print(fruits[1:3])

# clear() entfernt alle Elemente; die bestehende Liste ist danach leer.
# fruits.clear()
# print(fruits)

# List Comprehension: Erstellt eine neue Liste aus den passenden Elementen.
# Aufbau: [expression for item in source if condition]
# Hier werden nur Fruchtnamen mit mindestens fünf Zeichen übernommen.
# long_fruits = [fruit for fruit in fruits if len(fruit) >= 5]
# print(long_fruits)

# Sortieren: sorted() liefert eine neue Liste; fruits bleibt dabei unverändert.
sorted_fruits = sorted(fruits)
# sort() sortiert die bestehende Liste und gibt None zurück.
# fruits.sort()
fruits.extend(["Mango", "Lemon"])
print(fruits)
# Standardmäßig werden Strings nach Unicode-Codepunkten verglichen.
# Bei diesen Namen stehen Großbuchstaben dadurch vor Kleinbuchstaben.
fruits.sort()
print(fruits)
# Die zuvor erstellte Liste sorted_fruits enthält die später ergänzten Namen nicht.
# print(sorted_fruits)
# reverse() kehrt die aktuelle Reihenfolge um, ohne nach Werten zu sortieren.
# fruits.reverse()
# print(fruits)
# str.lower liefert den Vergleichsschlüssel; die gespeicherten Namen bleiben gleich.
# reverse=True sortiert absteigend, hier unabhängig von der Groß-/Kleinschreibung.
fruits.sort(key=str.lower, reverse=True)
print(fruits)

# Verschachtelte Listen: fruits[1] ist eine Liste, fruits[1][2] eine weitere Liste.
fruits = ["apple", ["banana", "lemon", ["kiwi", "watermelon"]], "mango"]
# print(fruits)
alias = fruits  # Zweiter Name für dieselbe Liste; es entsteht keine Kopie.
# Flache Kopie: neue äußere Liste, aber dieselben enthaltenen Unterlisten.
copy_of_fruits = fruits.copy()
# Tiefe Kopie: Kopiert hier auch alle verschachtelten Listen unabhängig vom Original.
# deep_copy_of_fruits = copy.deepcopy(fruits)
# Die Änderung an der geteilten Unterliste ist auch über alias und copy_of_fruits sichtbar.
fruits[1].append("cherry")
print(fruits)
print(alias)
print(copy_of_fruits)
# Eine zuvor erstellte tiefe Kopie wäre von dieser Änderung nicht betroffen.
# print(deep_copy_of_fruits)

# index() liefert den Index des ersten Treffers innerhalb der angesprochenen Liste.
# "cherry" steht hier an Index 3 der Unterliste, nicht der äußeren Liste.
print(fruits[1].index("cherry"))
fruits.append("")  # Auch ein leerer String zählt als ein Element.

print(fruits)
# count() zählt passende Werte nur auf der angesprochenen Listenebene.
print(fruits.count(""))
# len() zählt die vier Elemente der Unterliste; die tiefere Liste zählt als eines.
print(len(fruits[1]))
# pop(0) entfernt "kiwi" aus der tiefsten Liste und liefert den entfernten Wert.
remove_kiwi = fruits[1][2].pop(0)
print(remove_kiwi)
# Nach dem Entfernen würde index("kiwi") einen ValueError auslösen.
# print(fruits[1][2].index("kiwi"))
print(fruits)
