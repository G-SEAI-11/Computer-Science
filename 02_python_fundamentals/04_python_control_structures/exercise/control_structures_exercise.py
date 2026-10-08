print("---1. Basic If Condition---")
zahl = 3
# Genau eine der drei Verzweigungen wird ausgeführt.
if zahl > 0:
    print("Zahl ist positiv")
elif zahl == 0:
    print("Zahl ist null")
else:
    print("Zahl ist negativ")

print("---2. Grade Calculator---")
punkte = 65
# Die Bedingungen werden von oben nach unten geprüft.
# Dadurch wird die erste passende Note verwendet.
if punkte >= 90:
    note = "A"
elif punkte >= 80:
    note = "B"
elif punkte >= 70:
    note = "C"
elif punkte >= 60:
    note = "D"
else:
    note = "F"

print("Deine Note ist:", note)

print("---3. Ternary Operator Practice---")
alter = 26
# Der Ternary-Operator wählt einen von zwei Werten in einer Zeile aus.
status = "volljährig" if alter >= 18 else "minderjährig"
print(f"Die Person ist: {status}")

print("---4. For Loop over a List---")
car_list = ["Mercedes", "Audi", "Opel"]
# Bei jeder Wiederholung steht das nächste Listenelement in car zur Verfügung.
for car in car_list:
    print(car)


print("---5. For Loop with Conditions---")
# continue überspringt den Rest des aktuellen Schleifendurchlaufs.
for number in range(1, 11):
    if number % 2 != 0:
        continue
    print(number)

print("---6. While Loop Summation---")

# Die while-Schleife läuft, solange i höchstens 100 ist.
# i wird in jedem Durchlauf erhöht, damit die Schleife endet.
i = 0
x = 0
while i <= 100:
    x += i
    i += 1
print("While Schleife: Summe ist gleich", x)

summe = 0
# Dieselbe Summe wird hier mit einer for-Schleife berechnet.
for number in range(100 + 1):
    summe += number
print("For Schleife: Summe ist gleich", summe)

# sum berechnet die Summe aller Werte des range-Objekts direkt.
print("Sumbefehl: Summe ist gleich", sum(range(101)))

print("---7. Break out of a Loop---")
words = ["Cat", "Dog", "Apple", "Elephant", "House"]
# break beendet die Schleife sofort beim ersten Wort mit mehr als fünf Zeichen.
for word in words:
    if len(word) > 5:
        print("Ausbruch aus der Schleife bei:", word)
        break

print("---8. Nested Loops---")
people = ["Mike Tyson", "Cocaine Cowboy", "Michael Jackson"]
animals = ["Tiger", "Bear", "Chimpanzee"]
combinations = []

# Die innere Schleife wird für jede Person vollständig durchlaufen.
for person in people:
    for animal in animals:
        combinations.append((person, animal))
print(combinations)

print("---9. Loop with Else Clause---")

# Der else-Block einer for-Schleife wird nur ausgeführt,
# wenn die Schleife nicht mit break beendet wurde.
# number_check = input("enter a number from 1 to 10 ")
# number_list = [1, 2, 3, 4, 5]
# for x in number_list:
#     if x == int(number_check):
#         print(f"numer {x} was found")
#         break  # <<<< else block runs only, if the loop finished without a (break)
# else:
#     print("nummer not found")

print("---10. Pass Statement Usage---")
# pass ist ein Platzhalter und führt absichtlich keine Aktion aus.
for person in people:
    if person is animal:
        pass
    else:
        pass
print("Pass loop completed")

print("---11. Pattern matching---")

fruits = ["apple", "banana", "orange"]
veggies = ["carrot", "broccoli", "spinach"]
meat = ["chicken", "beef", "pork"]

item = "tomato"

# Ein match-Block vergleicht item mit mehreren möglichen Fällen.
# Die Guards prüfen zusätzlich, ob item in der jeweiligen Liste enthalten ist.
match item:
    case item if item in fruits:
        print("Fruit")
    case item if item in veggies:
        print("Veggie")
    case item if item in meat:
        print("Meat")
    case _:
        print("Something else")

match item:
    case _ if item in fruits:
        print("Fruit")
    case _ if item in veggies:
        print("Veggie")
    case _ if item in meat:
        print("Meat")
    case _:
        print("Something else")

# Pattern Matching kann auch zusammen mit einer for-Schleife eingesetzt werden.
# Hier wird das erste Element des Tupels geprüft und das zweite per Guard verglichen.
for comb in combinations:
    match comb[0]:
        case "Mike Tyson" if comb[1] == "Tiger":
            print("Mike Tiger")
        case "Cocaine Cowboy" if comb[1] == "Bear":
            print("Cocaine Bear")
        case "Michael Jackson" if comb[1] == "Chimpanzee":
            print("Michael Chimpanzee")
