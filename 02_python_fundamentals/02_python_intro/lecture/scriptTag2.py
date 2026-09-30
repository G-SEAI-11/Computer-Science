print("--- String-Grundlagen ---")


# quote_example = "It's Python"
# print(quote_example)

# quote_example = 'He said "Hello"'
# print(quote_example)


# single_quotes = 'hello'
double_quotes = "World"
multi_line = """This is a
multi-line
string"""

print(multi_line)


greeting = "Hello" + " " + "Python"
print("Begrüßung:", greeting)

laugh = "ha" * 3
print("Lachen:", laugh)

print("--- Stringmethoden ---")

# # Unveränderliche Strings
# * Stringmethoden liefern neue Strings zurück; der ursprüngliche String bleibt erhalten.
text = "  Hello Python World  "

print("Großbuchstaben:", text.upper())
print("Großbuchstaben:", text.lower())
print("Große Anfangsbuchstaben:", "hello python world".title())

# * strip entfernt nur Zeichen an den Rändern; Leerzeichen zwischen Wörtern bleiben erhalten.
print("[" + text.strip() + "]")
print("[" + text.lstrip() + "]")
print("[" + text.rstrip() + "]")

print(text.replace("Python", "JavaScript").strip())

# * Da das Ergebnis oben nicht an text zugewiesen wird, enthält text weiterhin den ursprünglichen Inhalt.
print(text)

javascript_for_the_win = text.replace("Python", "JavaScript").strip()

# * split ohne Argument fasst aufeinanderfolgende Leerraumzeichen als Trenner zusammen.
words = text.strip().split()
print(words)

# ! words verweist danach auf einen String statt auf eine Liste; die Zuweisung legt keinen festen Typ fest.
words = text.strip().upper()
print(words)


# text1 = "spam spam spam"

# * Das Beispiel verändert die von split erzeugte Liste, weil Strings selbst unveränderlich sind.
# * join erzeugt daraus einen neuen String; erst die Zuweisung ersetzt den Wert von text1.
# parts = text1.split(" ")
# parts[2] = "eggs"
# text1 = " ".join(parts)
# print(text1)


print("'Python' in text:", "Python" in text)
print('"JavaScript" not in text:', "JavaScript" not in text)


print("-- Stringormatierung ---")

name = "Alice"
age = 25
gpa = 3.85

# # Typen bei der Stringformatierung
# ! Das erste Beispiel würde einen TypeError auslösen: + wandelt age nicht automatisch in einen String um.
# * Die zweite Variante funktioniert, weil print seine Argumente einzeln in Text umwandelt.
# print("My name is " + name + " and I am " + age + " years old.")
# print("My name is", name, "and I am", age, "years old.")
# * Der f-String formatiert age als Text und speichert die aktuellen Werte; spätere Änderungen ändern messagef nicht.
messagef = f"My name is {name} and I am {age} years old."
print("f-String:", messagef)

price = 3.1
# * .2f rundet nur die Textdarstellung auf zwei Nachkommastellen; der Wert von price bleibt erhalten.
print(f"Preis: {price:.2f} €")


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# ! Unnummerierte Platzhalter übernehmen die Argumentreihenfolge: Hier landet itemno bei der Stückzahl und quantity bei der Artikelnummer.
print(myorder.format(itemno, quantity, price))
# print("My name is %s and I am %d years old." % (name, age))

print("--- Booleans und Wahrheitswerte ---")

is_sunny = True
is_raining = False

print("Sonnig:", is_sunny)
print("Regnerisch:", is_raining)

# truthy & falsy

# # Wahrheitswert statt inhaltlicher Bedeutung
# * Nicht leere Strings und Zahlen ungleich null sind truthy, unabhängig von ihrem Inhalt oder Vorzeichen.
# ! Auch ein String, der nur ein Leerzeichen enthält, ist nicht leer und ergibt daher True.
# True
print(bool("Hello"))
print(bool(" "))
print(bool(42))
print(bool(-42))

# False
print(bool(""))
print(bool(0))
print(bool(None))


temperature = 25
is_warm = temperature > 20
print("Warm:", is_warm)


# * Zuweisungsoperatoren
x = 10
x += 5
# x = x + 5
print("Nach +=5:", x)

x -= 3
print(x)

x *= 2
print(x)

# ! / liefert hier einen float; dadurch rechnen die folgenden Zuweisungen mit einem float weiter.
x /= 4
print("Nach /=4:", x)

# * // rundet den Quotienten nach unten; nach der vorherigen Division bleibt das Ergebnis hier ein float.
x //= 2
print("Nach //=2:", x)

x %= 2
print("Nach %=2:", x)

x = 2
x **= 3
# x = x**3
print("Nach **=3:", x)


print("--- Vergleichsoperatoren ---")

x = 10
y = 5

print(x == y)  # False
print(x != y)  # True
print(x > y)  # True
print(x < y)  # False
print(x >= 10)  # True
print(y <= 5)  # True

# # Stringvergleich und Groß-/Kleinschreibung
# * Strings werden Zeichen für Zeichen nach Unicode-Codepoints verglichen, nicht nach Länge oder sprachlichen Sortierregeln.
print("'apple' < 'banana':", "apple" < "banana")  # True
# ! Trotz des < im Ausgabetext prüft der Code hier ==; Groß- und Kleinschreibung unterscheiden sich beim Vergleich.
print("'Python' < 'python':", "Python" == "python")  # False
print("'z' < 'aa':", "z" < "aa")  # False
print("'a' < 'aa':", "a" < "aa")  # True

print("--- Logische Operatoren ---")

# # Kurzschlussauswertung logischer Operatoren
# * and wertet rechts nur weiter aus, wenn links truthy ist; or nur dann, wenn links falsy ist.
# ! and und or liefern einen Operanden zurück, nicht immer einen bool; hier sind die Operanden bool-Werte.
age = 10
has_license = True
can_drive = age >= 18 and has_license
print("Darf fahren:", can_drive)


is_weekend = False
is_holiday = True
can_relax = is_weekend or is_holiday
print("Kann entspannen:", can_relax)

is_raining = False
is_sunny = not is_raining

print("Sonnig:", is_sunny)


temperature = 25
is_summer = True
go_swimming = temperature > 20 and is_summer and not is_raining
print("Schwimmen gehen:", go_swimming)


# * Wir testen auf falsy & truthy
# ! is not None prüft gezielt auf einen fehlenden Wert; 0 ist ein vorhandener Wert, obwohl er falsy ist.
# * not value prüft dagegen den Wahrheitswert und ist auch bei anderen falsy Werten wie "" oder None True.
value = 0
print(value is not None)  # True
print(value != 0)  # False
print(not value)  # True


# # Unicode-Zeichen in Strings
# * len zählt Unicode-Codepoints, keine sichtbaren Zeichen; ein Emoji kann aus mehreren Codepoints bestehen.
print("Länge:", len(text))
print(len("Hallo"))
print(len("ä"))
print(len("👍"))
print(len("👍🏽"))  # 2. Daumen + Hautfarbe

print("Anzahl von o:", text.count("o"))


sample = "Python lernen"
# ! Ein einzelner Index außerhalb des Strings löst einen IndexError aus; ein Slice kürzt zu große Grenzen auf die vorhandene Länge.
print(sample[0])
print(sample[-1])
print(sample[:6])

for char in sample:
    print(char)


# # Gleicher Inhalt und dasselbe Objekt
# * same_scores verweist auf dieselbe Liste wie scores; eine Änderung an dieser Liste wäre über beide Namen sichtbar.
# * other_score wird als separate Liste erzeugt; gleicher Inhalt bedeutet keine gemeinsame Objektidentität.
scores = [10, 20]
same_scores = scores
other_score = [10, 20]

# ! == vergleicht bei Listen den Inhalt, is die Objektidentität; is eignet sich nicht als Ersatz für einen Inhaltsvergleich.
print(scores == other_score)  # Vergleichen den Inhalt
print(scores is same_scores)  # Vergleichen, ob es das selbe Objekt ist
print(scores is other_score)
print(scores is not other_score)
print(scores == other_score)
