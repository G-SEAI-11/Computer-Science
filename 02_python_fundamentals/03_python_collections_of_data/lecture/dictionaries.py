print("---1. Dictionary erstellen und ausgeben---")
# Ein Dictionary speichert Daten als Schlüssel-Wert-Paare.
person = {"name": "Alex", "age": 30, "city": "Berlin"}
print(person)
# len() gibt die Anzahl der Schlüssel-Wert-Paare zurück.
print("Länge des Dictionary:", len(person))

print("---2. Werte auslesen und Schlüssel prüfen---")
# Über den Schlüssel kann ein Wert direkt ausgelesen werden.
print(person["name"])
# print(person["zipcode"]) # erzeugt einen KeyError, da der Schlüssel nicht vorhanden ist
# get() liefert None oder einen selbst gewählten Standardwert, wenn der Schlüssel fehlt.
print("Aufruf über get():", person.get("city"))
print("Aufruf über get() mit default:", person.get("email", "email not provided"))

print("---3. Schlüssel/Werte/Paare ansehen---")
# .keys(), .values(), .items()
# Diese Methoden liefern Ansichten auf Schlüssel, Werte beziehungsweise Paare.
print(person.keys())
print(person.values())
print(person.items())

snapshot_values = person.values()
# Eine Ansicht kann mit list() in eine echte Liste umgewandelt werden.
values_list = list(snapshot_values)
print(values_list)

print("---4.Werte ändern und Einträge ergänzen---")
# Durch Zuweisung wird ein vorhandener Wert geändert.
person["city"] = "Hamburg"
print(person)
# update() ändert mehrere Werte und fügt neue Schlüssel hinzu.
person.update(
    {"age": 31, "occupation": "Engineer", "country": "Germany", "gender": "male"}
)
print(person)

print("---5. Einträge entfernen---")
# pop() entfernt den angegebenen Schlüssel und gibt seinen Wert zurück.
print("Eintrag der entfernt wird:", person.pop("occupation"))
print(person)
# popitem() entfernt das zuletzt eingefügte Schlüssel-Wert-Paar.
print("Letzte Eintrag wird über .popitem() entfernt:", person.popitem())
# Mit del wird ein Eintrag entfernt, ohne seinen Wert zurückzugeben.
del person["country"]
print(person)

# copy() erstellt eine flache Kopie des Dictionaries.
person_copy = person.copy()
print(person_copy)
# clear() entfernt alle Einträge aus dem Dictionary.
person_copy.clear()
print(person_copy)

print("---6.Referenz und Copy---")
# Eine Zuweisung erzeugt nur eine weitere Referenz auf dasselbe Dictionary.
another_person = person
# copy() und dict() erzeugen dagegen ein neues Dictionary.
another_copy = person.copy()
person_dict_copy = dict(person)
print("Original", person)
print("Referenz:", another_person)
print(".copy():", another_copy)
print("dict():", person_dict_copy)
# Änderungen über die Referenz wirken sich auf das Original aus.
person["age"] = 32
print("Original", person)
print("Referenz:", another_person)
print(".copy():", another_copy)
print("dict():", person_dict_copy)

print("---7.setdefault() und .fromkeys()")
# setdefault() fügt den Schlüssel nur hinzu, wenn er noch nicht vorhanden ist.
person.setdefault("hometown", "Munich")
print(person)
# fromkeys() erzeugt ein Dictionary mit mehreren Schlüsseln und einem Startwert.
contact_defaults = dict.fromkeys(["email", "phone", "fax"], "not provided")
print(contact_defaults)

print("---8.Verschachtelung---")
# Dictionaries können weitere Dictionaries als Werte enthalten.
person["address"] = {"street": "Musterstraße", "number": 20}
print(person)
print(person["address"]["street"])

# Eine flache Kopie kopiert das äußere Dictionary, aber nicht verschachtelte Werte.
shallow_copy = person.copy()
print(shallow_copy)
person["address"]["street"] = "Beispielstraße"
print(person)
print(shallow_copy)

# update() mit einem neuen Dictionary ersetzt den bisherigen verschachtelten Wert.
person.update({"address": {"street": "Musterstraße"}})
print(person)
