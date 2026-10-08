print("---1. Create and print a dictionary")
# Ein Dictionary speichert Werte unter eindeutigen Schlüsseln.
person = {"name": "Michael", "age": 35, "city": "Hamburg"}
print(person)

print("---2. Access Dictionary Elements---")
# get() liefert den Wert zum Schlüssel oder den angegebenen Ersatzwert,
# wenn der Schlüssel nicht vorhanden ist.
name = person.get("name", None)
test_name = person.get("großer_zeh", None)
print(name)
print(test_name)
# Mit eckigen Klammern kann auf einen vorhandenen Schlüssel zugegriffen werden.
# Bei einem unbekannten Schlüssel entsteht dabei ein KeyError.
# print(person["name"])
# Diese Methoden liefern alle Schlüssel, Werte oder Schlüssel-Wert-Paare.
print(person.keys())
print(person.values())
print(person.items())

print("---3. Check for Key Existence---")
# Der Operator in prüft, ob ein Schlüssel im Dictionary existiert.
print("Age in person:", "age" in person)

print("---4. Change and Update Dictionary Elements---")
# Ein vorhandener Schlüssel kann direkt überschrieben werden.
person["city"] = "Munich"
# update() ändert mehrere Werte und fügt neue Schlüssel hinzu.
person.update({"age": 26, "occupation": "IT Informatiker"})
print(person)

print("---5. Add New Items to the Dictionary---")
# Ein neuer Schlüssel wird durch eine Zuweisung hinzugefügt.
person["country"] = "USA"
print(person)
# Auch mit update() können neue Einträge ergänzt werden.
person.update({"hobby": "cycling"})
print(person)

print("---6. Remove Items from the Dictionary---")
# pop() entfernt den angegebenen Schlüssel und gibt seinen Wert zurück.
print(person.pop("country"))
# popitem() entfernt und liefert das zuletzt eingefügte Schlüssel-Wert-Paar.
print(person.popitem())
# del löscht einen Eintrag, gibt aber keinen Wert zurück.
del person["occupation"]
print(person)
# clear() würde alle Einträge aus dem Dictionary entfernen.
# print(person.clear())

print("---7. Copy a Dictionary---")
# copy() erstellt eine flache Kopie des Dictionaries.
person_copy = person.copy()
person["age"] = 40
# Die Änderung betrifft nur das Original, nicht die Kopie.
print("Original:", person)
print("Kopie:", person_copy)
# dict() kann ebenfalls ein neues Dictionary aus person erstellen.
person_constructor_copy = dict(person)
print(person_constructor_copy)

# robin = dict([("name", "robin"), ("profession", "sidekick")])
# print(robin)

print("---8. Using setdefault()---")
# setdefault() liefert den vorhandenen Wert eines Schlüssels.
# Fehlt der Schlüssel, wird er mit dem angegebenen Wert angelegt.
city = person.setdefault("city", "Berlin")
print("City:", city)
occupation = person.setdefault("occupation", "Engineer")
print("Occupation:", occupation)
print("Dictionary:", person)
