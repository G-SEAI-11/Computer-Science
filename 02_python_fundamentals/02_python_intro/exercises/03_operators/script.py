# Step 1: Arithmetic Operators
a = 15
b = 4
# Perform arithmetic operations
print(a + b)
print(a - b)
print(a * b)
# # Division und Rest
# * / liefert hier einen float; // rundet den Quotienten zur nächstkleineren ganzen Zahl ab.
# ! Bei negativen Ergebnissen rundet // daher nicht Richtung 0: -15 // 4 ergibt -4.
print(a / b)
print(a // b)
# * % liefert den Rest passend zur Division mit //: a == (a // b) * b + a % b.
print(a % b)
print(a**b)

# Step 2: Assignment Operators
x = 10
# Modify x using assignment operators
# * Jede verkürzte Zuweisung verwendet den aktuellen Wert von x; die Änderungen bauen aufeinander auf.
x += 5  # x = x + 5
print("Nach +=:", x)
x -= 3  # x = x - 3
print("Nach -=:", x)
x *= 2  # x = x * 2
print("Nach *=:", x)
# * Auch /= verwendet echte Division; x enthält danach einen float, selbst bei einem ganzzahligen Ergebnis.
x /= 4  # x = x / 4
print("Nach /=:", x)

# Step 3: Comparison Operators
a = 15
b = 4
# Compare a and b
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Step 4: Logical Operators
is_python_fun = True
is_javascript_fun = False
# Combine Boolean variables
# * and wertet rechts nur aus, wenn links wahr ist; or nur, wenn links falsch ist (Short-Circuit).
# ! Allgemein geben and und or einen Operanden zurück; hier sind die Operanden bereits bool-Werte.
print(is_python_fun and is_javascript_fun)
print(is_python_fun or is_javascript_fun)
print(not is_javascript_fun)


# Step 5: Identity Operators
# # Identität, Wertgleichheit und gemeinsame Referenzen
# * list2 = list1 erstellt keine Kopie: Beide Namen verweisen auf dieselbe veränderliche Liste.
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
# Check identities
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)
# Check if list1 is list3
# * is prüft, ob es dasselbe Objekt ist; == vergleicht bei diesen Listen den Inhalt.
# ! Gleicher Inhalt garantiert keine gemeinsame Identität; is ersetzt keinen Wertvergleich.
print("list3 is list1:", list1 is list3)  # False (Adresse unterschiedlich)
print(list1 == list3)  # True (Inhalt gleich)

# * Die Änderung betrifft das gemeinsame Listenobjekt und ist deshalb auch über list2 sichtbar.
list1[0] = 99
print(list1)
print(list2)
print(list3)

# * Diese Zuweisung bindet nur list1 an eine neue Liste; list2 verweist weiterhin auf die bisherige Liste.
list1 = ["Haus"]
print(list1)
print(list2)
print(list3)


# Step 6: Membership Operators
text = "Python programming is fun!"
# Check membership
# * Bei Strings prüft in eine Teilzeichenfolge, keine Wortgrenzen; Groß- und Kleinschreibung zählen.
print("Python" in text)
print("JavaScript" not in text)

# Step 7: Bitwise Operators (Bonus)
a = 5
b = 3
# Perform bitwise operations
# # Operatoren auf einzelnen Bits
# * 5 ist binär 101, 3 ist 011: & behält gemeinsame Bits, | alle gesetzten Bits, ^ nur unterschiedliche Bits.
# ! & und | arbeiten hier auf Zahlenbits; sie haben nicht das Short-Circuit-Verhalten von and und or.
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
# * Eine Linksverschiebung um ein Bit multipliziert diese positiven Ganzzahlen mit 2.
print("a << 1:", a << 1)
print("b << 1:", b << 1)
# * Python-Ganzzahlen haben keine feste Bitbreite; die Bit-Invertierung ergibt deshalb ~a == -a - 1.
# * Oder allgemeiner ausgedrückt: ~x = -(x + 1)
print("~a:", ~a)

# Step 8: Operator Precedence
# Write expressions with precedence
# * ** wird vor * und * vor + ausgewertet; Klammern erzwingen eine andere Gruppierung.
# ! In Python bedeutet ^ bitweises XOR, nicht Potenzieren; die folgenden Rechenschritte nutzen mathematische Notation.
print(2 + 3 * 4**2)
# 2 + 3 * 16
# 2 + 48
# 50
print((2 + 3) * 4**2)
# 5 * 16
# 80
print(((2 + 3) * 4) ** 2)
# (5 * 4) ^2
# 20^2
# 400
