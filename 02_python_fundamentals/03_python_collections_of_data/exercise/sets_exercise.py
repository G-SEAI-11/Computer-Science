print("---1. Create a Set---")
# Ein Set speichert eindeutige Werte ohne feste Reihenfolge.
früchte = {"Apfel", "Banane", "Orange", "Mango", "Kiwi"}
print(früchte)

print("---2. Check Membership--")
# Mit in lässt sich prüfen, ob ein Wert im Set enthalten ist.
if "Banane" in früchte:
    print("Ja, Banane ist im Set vorhanden.")
else:
    print("Nein, Banane ist nicht im Set vorhanden.")

print("---3. Add and Update Items---")
# add() fügt ein einzelnes Element hinzu.
früchte.add("Wassermelone")
print(früchte)

# update() fügt mehrere Elemente aus einem anderen Set hinzu.
mehrere_früchte = {"Ananas", "Erdbeere"}
früchte.update(mehrere_früchte)
print(früchte)

print("---4. Remove Items---")
# remove() entfernt ein Element und löst einen Fehler aus, wenn es nicht existiert.
früchte.remove("Banane")
print("Entferne eine Frucht mit remove():", früchte)

# discard() entfernt ein Element ohne Fehler, falls es nicht vorhanden ist.
früchte.discard("Banane")
print("Nach discard(Banane)passiert nichts:", früchte)

# pop() entfernt ein beliebiges Element und gibt es zurück.
entfernte_frucht = früchte.pop()
print(entfernte_frucht)
print(früchte)

# copy() erstellt eine unabhängige Kopie, die mit clear() geleert werden kann.
früchte_kopie = früchte.copy()
früchte_kopie.clear()
print("Nach dem clear() der Kopie:", früchte_kopie)

print("---5. Set Operations---")
set_a = {"Banane", "Mango", "Kiwi", "Pfirsich"}
set_b = {"Orange", "Ananas", "Pfirsich", "Kirsche"}
print("set a:", set_a)
print("set b:", set_b)
# union() verbindet beide Sets und entfernt doppelte Werte.
print("Union:", set_a.union(set_b))

# intersection() liefert nur die gemeinsamen Werte beider Sets.
print("Intersections:", set_a.intersection(set_b))

# difference() liefert Werte aus set_a, die nicht in set_b vorkommen.
print("Difference:", set_a.difference(set_b))

# symmetric_difference() liefert Werte, die nur in einem der beiden Sets vorkommen.
print("Symmetric Difference:", set_a.symmetric_difference(set_b))

print("---6. In-place Set Operations---")
set_a_copy = set_a.copy()
set_b_copy = set_b.copy()

# Die Update-Methoden verändern das Set direkt, statt ein neues zurückzugeben.
set_a_copy.difference_update(set_b)
print("Nach Difference Update:", set_a_copy)

set_a_copy = set_a.copy()
set_a_copy.intersection_update(set_b)
print("Nach Interesection Update:", set_a_copy)

set_a_copy = set_a.copy()
set_a_copy.update(set_b)
print("Nach Update:", set_a_copy)

print("---7. Relational Methods---")
small_set = {"football", "baseball", "basketball"}
large_set = {
    "football",
    "baseball",
    "basketball",
    "cricketball",
    "icehockeyball",
    "beachball",
}
print(small_set.issubset(large_set))
# issuperset() prüft, ob large_set alle Werte aus small_set enthält.
print(large_set.issuperset(small_set))

# isdisjoint() ist True, wenn die Sets keine gemeinsamen Werte haben.
print(small_set.isdisjoint(set_a))
