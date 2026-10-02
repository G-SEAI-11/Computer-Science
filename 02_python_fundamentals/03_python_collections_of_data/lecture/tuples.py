# Vergleich: Liste vs. Tupel
# Ein Tupel ist unveränderlich und wird mit runden Klammern erstellt.
fruits = ("apple", "banana", "kiwi", "lemon")
print("---Tupel erstellen und ausgeben---")
print(fruits)
print(type(fruits))
print(len(fruits))

# Ein Tupel mit nur einem Element braucht ein Komma, sonst ist es kein Tupel.
print("---Tupel mit nur einem Element---")
single_fruit = ("apple",)
print(single_fruit)

# Zugriff auf einzelne Elemente und Bereiche.
# Bei Slicing ist der Start inklusive, das Ende exklusive.
print("---Auf Positionen und Bereiche zugreifen---")
print(fruits[-1])
print(fruits[0])
print(fruits[0:2])
print(fruits[1:])

# Prüfung, ob ein Wert im Tupel enthalten ist.
print("---Enthalten in---")
search_fruit = "apple"
print(search_fruit in fruits)

# Typumwandlungen sind bewusst möglich, aber nicht immer sinnvoll.
print("---Bewusste Typumwandlung---")
fruit_list = list(fruits)
print(fruit_list)
fruit_list.pop(1)
print(fruit_list)
converted_tuples = tuple(fruit_list)
print(converted_tuples)

# Entpacken: Jeder Wert wird einer Variablen zugewiesen.
print("---Unpacking---")
first_fruit, second_fruit, third_fruit, fourth_fruit = fruits
print(first_fruit, second_fruit, third_fruit, fourth_fruit)

# Mit * werden die restlichen Elemente in einer Liste gesammelt.
first_fruit, *remaining_fruits = fruits
print(first_fruit, remaining_fruits)

first_fruit, *remaining_fruits, last_fruit = fruits
print(first_fruit, remaining_fruits, last_fruit)

# Tupel lassen sich ebenfalls miteinander verbinden.
print("---Verbinden---")
extra_fruits = ("watermelon", "honeymelon", "papaya")
combined_fruits = fruits + extra_fruits
print(combined_fruits)

# Wiederholen eines Tupels erzeugt eine neue Folge mit mehrfachen Elementen.
print("\n---Wiederholen---")
repeated_fruits = fruits * 2
print(repeated_fruits)

# count() zählt Vorkommen, index() liefert die erste Position eines Werts.
print("---Index und Count---")
print(repeated_fruits.count("kiwi"))
print(fruits)
print(fruits.index("banana"))

# Verschachtelte Tupel können innere, veränderbare Elemente enthalten.
print("---Vertiefung---")
nested_fruits = ("apple", ("lemon", ["banana", "cherry"]))
print(nested_fruits)
nested_fruits[1][1].append("orange")
print(nested_fruits)
