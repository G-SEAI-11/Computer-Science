# Step 1: Create Strings
first_name = "Mirko"
last_name = "Strauss"
bio = """Ich liebe Sport und Fitness.
Ich reise gerne mit meiner Frau."""

# Step 2: Access Characters and Slice Strings
# # Zeichenpositionen und Ausschnitte
# * Indizes beginnen bei 0; negative Indizes zählen vom Ende des Strings aus.
# * Beim Slicing ist die Endposition ausgeschlossen: 0:10 umfasst die ersten zehn Zeichen.
# ! Ein einzelner Index außerhalb des Strings löst IndexError aus; ein Slice wird dagegen begrenzt.
print(first_name[0])
print(last_name[-1])
print(bio[0:10])  # slicing

# Step 3: Loop Through a String
# * Die Schleife liefert einzelne Zeichen, einschließlich Leerzeichen und Zeilenumbrüchen.
for sauerkraut in bio:
    # print("Der Buchstabe ist: " + sauerkraut)
    print(f"Der Buchstabe ist: {sauerkraut}")

# Step 4: String Length
# * Auch Leerzeichen und der Zeilenumbruch im mehrzeiligen String zählen zur Länge.
print(len(bio))

# Step 5: Check Substrings
# * in sucht eine zusammenhängende Zeichenfolge und unterscheidet Groß- und Kleinschreibung.
print("Sport" in bio)
# print("Sport" in [bio][0])
# * [bio][0] liefert wieder den String bio; die zusätzliche Liste ändert die Teilstring-Suche nicht.
print("JavaScript" not in bio)


# Step 6: Modify Strings
# # Strings sind unveränderlich
# * upper(), lower(), strip() und replace() liefern neue Strings; erst die Zuweisung übernimmt das Ergebnis.
print(first_name.upper())
print(last_name.lower())
# ! strip() entfernt nur äußere Leerzeichen und Zeilenumbrüche, keine innerhalb des Textes.
bio = bio.strip().replace("Sport", "coding")

# * split() ohne Argument trennt an zusammenhängenden Whitespace-Zeichen, auch am Zeilenumbruch.
words = bio.split()
print(first_name, last_name, words)

# Step 7: Concatenate Strings
full_name = first_name + " " + last_name
print(full_name)

# Step 8: String Formatting
# * Formatierung bettet Werte in Text ein, ohne dass sie vorher manuell in Strings umgewandelt werden müssen.
print(f"Hello, my name is {full_name} and I love Python!")
# * :.2f stellt den Zahlenwert mit zwei Nachkommastellen dar; der ursprüngliche Wert bleibt unverändert.
print("My full name is {} and I am {:.2f} years old.".format(full_name, 50))  # noqa: UP032

# Step 9: Escape Characters
# * Der Backslash verhindert, dass ein Anführungszeichen den String beendet; er selbst wird nicht ausgegeben.
text = 'He said, "Python\'s great!"'
print(text)

print("'Jeder' Programmierer sagt: \"Python is great!\"")

# Bonus: Use String Methods
print(bio.center(100, "."))

print("count of letter a in my full_name", full_name.count("a"))
