print("---1. Create and Print a List---")
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
print(wochentage)

print("\n---2. Access Elements by Index and Negative Index")
# Mit positiven Indizes zählen wir vom Anfang, mit negativen vom Ende der Liste.
print(wochentage[0])
print(wochentage[-1])
print(wochentage[-2])

print("\n--3. Slice a List---")
# Ein Slice gibt einen bestimmten Ausschnitt der Liste zurück.
print(wochentage[1:4])
print(wochentage[:3])
print(wochentage[1:])

print("\n---4. Check if an Item Exists---")
# Mit dem Operator "in" prüfen wir, ob ein Element enthalten ist.
if "Donnerstag" in wochentage:
    print("Ja, Donnerstag ist in der Liste.")
if "Wochenende" in wochentage:
    print("True")
else:
    print("False")

print("Ist Freitag enthalten?", "Freitag" in wochentage)

print("\n---5. Add Items---")
# append() fügt am Ende hinzu, insert() an einer bestimmten Position.
wochentage.append("Jahr")
wochentage.insert(1, "Monat")
print(wochentage)

print("\n---6. Change Items---")
# Einzelne Elemente und auch ganze Bereiche können ersetzt werden.
wochentage[-1] = "Samstag"
wochentage[0:3] = ["Montag", "Dienstag"]
print(wochentage)

print("\n---7. Remove Items---")
# remove() löscht nach Wert, pop() nach Index und gibt das Element zurück.
wochentage.remove("Montag")
wochentage.pop(4)
print(wochentage)
# wochentage.clear()
# print(wochentage)

print("\n---8. Copy a List---")
# copy() erstellt eine unabhängige flache Kopie der Liste.
my_copy = wochentage.copy()
# my_copy = wochentage[:]
my_copy[1] = "Sonntag"
print(wochentage)
print(my_copy)

print("\n---9. Concatenate and Extend---")
wochentage_1 = ["Montag", "Dienstag"]
wochentage_2 = ["Mittwoch", "Donnerstag"]
# Mit + entsteht eine neue Liste; die ursprünglichen Listen bleiben unverändert.
wochentage_3 = wochentage_1 + wochentage_2
print("Mit Plus zusammenführen", wochentage_3)
# extend() erweitert die erste Liste direkt um die Elemente der zweiten Liste.
wochentage_1.extend(wochentage_2)
print("Mit extend() zusammenführen", wochentage_1)

print("\n---10. Sort and Reverse---")
zahlen = [7.2, 9, 1, 5]
# sorted() erstellt eine sortierte Kopie, sort() verändert die ursprüngliche Liste.
sortiere_neue_liste = sorted(zahlen)
print("Nummer mit sorted():", sortiere_neue_liste)
zahlen.sort()
# reverse() dreht die Reihenfolge der Elemente um.
print("Nach sort():", zahlen)
zahlen.reverse()
print("Nach reverse():", zahlen)

print("\n---11. Count and Index---")
# count() zählt Vorkommen, index() liefert die Position des ersten Vorkommens.
anzahl_wochentage = wochentage.count("Mittwoch")
print(anzahl_wochentage)
stelle_mittwoch = wochentage.index("Mittwoch")
print(stelle_mittwoch)
print(wochentage)

print("\n---12. List Comprehension---")
# Listen lassen sich mit einer List Comprehension aus mehreren Listen erzeugen.
neue_liste = wochentage + zahlen
print(neue_liste)
# Hier werden nur Texte mit dem Buchstaben "t" ausgewählt und großgeschrieben.
ganz_neue_liste = [
    item.upper() for item in neue_liste if isinstance(item, str) and "t" in item
]
print(ganz_neue_liste)


wochentage = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag",
]
# Wochenende bleibt unverändert, alle anderen Tage erhalten einen neuen Text.
neue_wochentage = [
    "scheiß Tag" if wt != "Samstag" and wt != "Sonntag" else wt for wt in wochentage
]
print(neue_wochentage)

# Nur Wochentage mit mehr als acht Zeichen werden ausgewählt und großgeschrieben.
neue_wochentage2 = [wochentag.upper() for wochentag in wochentage if len(wochentag) > 8]
print(wochentage)
print(neue_wochentage2)
