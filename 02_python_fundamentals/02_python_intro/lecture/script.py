print("--- Python-Syntax ---")

# Das ist ein einzeiliger Kommentar
# ! Der folgende Block ist ein Stringliteral, kein mehrzeiliger Kommentar.
# * Da der String hier weder zugewiesen noch ausgegeben wird, erscheint keine Ausgabe.
"""
Das ist ein mehrzeiliger String.
Hier könnt ihr mehrere Zeilen schreiben.
Nützlich für die Dokumentation!
"""

name = "John"
print("Hello,", name)

print("--- Variablen und Typprüfung ---")

student_name = "Bob"  # Variablen schreibweise mit snake_case
is_enrolled = True


print("Typ von student_name:", type(student_name))
print("Typ von is_enrolled:", type(is_enrolled))

# # Typen gehören zu Objekten
# * type() zeigt den Typ des aktuell gebundenen Objekts; der Name selbst
# * ist nicht dauerhaft auf einen Typ festgelegt.
my_variable = 10
print("my_variable vor der Neuzuweisung:", type(my_variable))

# * Die Neuzuweisung bindet my_variable an einen String. Die ursprüngliche
# * Zahl wird dabei nicht in einen String umgewandelt.
my_variable = "11"
print("my_variable nach der Neuzuweisung:", type(my_variable))

# * b = a bindet beide Namen an dasselbe Objekt. Die spätere Neuzuweisung
# * von a ändert nur dessen Bindung; b verweist weiterhin auf die Zahl 10.
# a = 10
# b = a
# a = "11"

# print(type(a), type(b))
# print(a, b)
# print(a == b)

# ! b = a kopiert die Liste nicht. b[1] = 11 verändert das gemeinsame
# ! Listenobjekt; die Änderung ist deshalb auch über a sichtbar.
# a = [10, "hello", 42, []]
# b = a
# b[1] = 11
# print(a)


print("--- Typumwandlung ---")
name = "Elizabeth"
age = 25
# * str(age) liefert einen String für die Verkettung mit +; age bleibt ein int.
# ! Ein String und ein int lassen sich nicht direkt mit + verketten.
age_str = str(age)  # "25"
print("Alter als String:", "I am " + age_str + " years old")
# * Bei print mit mehreren Argumenten entfällt die vorherige str()-Umwandlung.
# print("I am", age, "years old")

# print("Alter:", age, type(age))
# print("age_str:", age_str, type(age_str))

print("Name:", name, "Alter:", age)


# ! float("fünf") würde ValueError auslösen: Nicht jeder String stellt eine Zahl dar.
float_example = float("5")
# * bool(1) ist True, weil Zahlen außer 0 als wahr gelten.
# ! bool("False") wäre ebenfalls True, denn jeder nichtleere String gilt als wahr.
bool_example = bool(1)

print("float(5):", float_example)
print("bool(1):", bool_example)


def calculate_grade(sauerkraut):
    if sauerkraut >= 90:
        print("Sehr gut")


# ! Der Vergleich mit 90 erwartet hier eine Zahl: "95" als Argument
# ! würde wegen des Vergleichs von str und int einen TypeError auslösen.
calculate_grade(95)
calculate_grade(67)

print("--- Mit Zahlen arbeiten ---")

a = 10
b = 3

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
# * / liefert auch bei zwei int-Werten einen float. // rundet den Quotienten
# * zur kleineren ganzen Zahl ab: -10 // 3 wäre deshalb -4 und nicht -3.
print("a / b:", a / b)
print("a // b:", a // b)  # floor division
print("a % b:", a % b)  # Modulo
print("a ** b:", a**b)  # Potenz

# * Für diese gemischte Addition wird der int-Wert als float behandelt;
# * deshalb hat auch das Ergebnis den Typ float.
result = 5 + 2.5
print("5 + 2.5:", result, type(result))


# # Many values to multiple variables
# a, b, c = 1, 2, 3  # Assign multiple values at once
# print(a, b, c)

# # One value to multiple variables
# x = y = z = 10  # Assign the same value to multiple
# print(x, y, z)


quote_example = "It's Python"
print(quote_example)

quote_example = 'He said "Hello"'
print(quote_example)
