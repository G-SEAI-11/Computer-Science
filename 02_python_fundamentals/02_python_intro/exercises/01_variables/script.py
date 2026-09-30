# Step 1: Create variables:
name = "Ahmed"
age = 26
height = 1.70

# Step 2: Print the variables:
print("Name:", name, "Age:", age, "Height:", height)


# Step 3: Check the type of the variables:
# # Datentypen der zugewiesenen Werte
# * Der Typ gehört zum Wert, auf den der Variablenname verweist, nicht zum Namen selbst.
# * Eine spätere Zuweisung kann denselben Namen daher an einen Wert eines anderen Typs binden.
print(type(name))
print(type(age))
print(type(height))

# Step 4: Casting
# # Zahlen für die Textausgabe umwandeln
# * str() erzeugt einen String; age und height behalten dabei ihre numerischen Werte.
# ! Bei der Verkettung mit + müssen hier alle Teile Strings sein; eine Zahl würde TypeError auslösen.
age_str = str(age)
height_str = str(height)

print(
    "Ich heiße "
    + name
    + " und bin "
    + age_str
    + " Jahre alt. Und ich bin "
    + height_str
    + " Meter groß."
)
# * Separate print()-Argumente und f-Strings wandeln Zahlen für die Ausgabe automatisch in Text um.
print(
    "Ich heiße", name, "und bin", age, "Jahre alt. Und ich bin", height, "Meter groß."
)
print(f"Ich heiße {name} und bin {age} Jahre alt. Und ich bin {height} Meter groß.")


# Bonus: Global Variable (Bonus)
# # Globale und lokale Variablen
global_message = "Hallo, dies ist eine globale Nachricht."
print("Vor der Funktion:", global_message)


def update_global_message():
    # * global sorgt dafür, dass die folgende Zuweisung den Namen auf Modulebene neu bindet.
    # ! Ohne global würde die Zuweisung eine lokale Variable erzeugen und die globale Nachricht unverändert lassen.
    global global_message
    global_message = "Hallo, vom funktionalen Gültigkeitsbereich (functional scope)"
    locale_message = "Mich bekommst du global nicht!"
    print("In der Funktion:", global_message)
    print(locale_message)


# ! update_global_message wird hier nicht aufgerufen; deshalb bleibt global_message unverändert.
print("Nach der Funktion:", global_message)
# print("locale_message:", locale_message)
# ! Auch nach einem Funktionsaufruf wäre locale_message hier nicht zugänglich: Der Name ist lokal.
# * Das auskommentierte Beispiel würde deshalb beim Aktivieren einen NameError auslösen.
