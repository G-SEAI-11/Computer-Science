print("---Set anlegen---")
fruits = {"apple", "banana", "cherry", "apple", "mango", "pear"}  # noqa: B033
print(fruits)
print(type(fruits))
print("Length of set:", len(fruits))

print("---Leeres Set---")
# Ein leeres Set wird mit set() erstellt, da {} ein leeres Dictionary ergibt.
set_leer = set()
tuple_leer = ()
print(set_leer)
print(type(set_leer))
print(tuple_leer)
print(type(tuple_leer))

print("---Set aus einer Liste---")
fruits_list = ["apple", "banana", "cherry", "apple", "mango", "pear"]
unique_fruits = set(fruits_list)
print(fruits_list)
print(unique_fruits)

print("---Enthalten sein prüfen---")
search_fruit = "apple"
print("Ist die gesuchte Frucht enthalten:", search_fruit in unique_fruits)

print("---Werte dem Set hinzufügen---")
fruits.add("orange")
print(fruits)
fruits.update({"lemon", "kiwi"})
print(fruits)

print("---Werte aus dem Set entfernen---")
fruits.remove("banana")
print(fruits)
# discard() entfernt den Wert ebenfalls, löst bei einem fehlenden Wert aber keinen Fehler aus.
fruits.discard("watermelon")
print(fruits)

print("---Set kopieren---")
copy_fruits = fruits.copy()
print(fruits)
print(copy_fruits)

print("---Wert per pop() rausnehmen---")
# Sets sind ungeordnet; pop() entfernt daher ein beliebiges Element.
removed_fruit = copy_fruits.pop()
print("Entfernter Wert:", removed_fruit)
print("Kopie vom Set fruits:", copy_fruits)
print("Original Set fruits:", fruits)

print("---Set leeren mit clear()---")
copy_fruits.clear()
print(copy_fruits)

print("---Sets vergleichen---")
basket_a = {"apple", "banana", "cherry"}
basket_b = {"banana", "cherry", "mango"}
print(basket_a)
print(basket_b)

print("---Sets verbinden---")
all_fruits = basket_a.union(basket_b)
print(all_fruits)

print("Die Union aus basket_a und basket_b:", all_fruits)

print("---Schnittmenge von Sets---")
common_fruits = basket_a.intersection(basket_b)
print(common_fruits)

print("---Difference von Sets---")
only_a = basket_a.difference(basket_b)
only_b = basket_b.difference(basket_a)
print(only_a)
print(only_b)

print("---Symmetric Difference von Sets---")
different_fruits = basket_a.symmetric_difference(basket_b)
print(different_fruits)


print("---Set mit Update Methoden verändern---")
print("---Set mit Difference Update Methode verändern---")
updated_fruits = basket_a.copy()
updated_fruits.difference_update(basket_b)
print("Nach difference_update():", updated_fruits)


print("---Set mit Intersection Update Methode verändern---")
updated_fruits = basket_a.copy()
updated_fruits.intersection_update(basket_b)
print("Nach intersection_update():", updated_fruits)

print("---Set mit Symmetric Difference Update Methode verändern---")
updated_fruits = basket_a.copy()
updated_fruits.symmetric_difference_update(basket_b)
print("Nach symmetric_difference_update():", updated_fruits)

print("---Subset/Teilmengen---")
basket_b.remove("mango")
print(basket_b.issubset(basket_a))
print(basket_a.issubset(basket_b))

print("---Superset/Obermengen---")
print(basket_a.issuperset(basket_b))
print(basket_b.issuperset(basket_a))

print("---Disjoint/Disjunkt----")
print(basket_a.isdisjoint(basket_b))
basket_c = {"watermelon", "kiwi"}
print(basket_c.isdisjoint(basket_a))


# Beispiele für update() mit Sets
# fruit_set = set({"papaya", "apple", "pear", "cherry", "orange"})
# fruit_other_set = {"grape", "coconut"}
# fruit_set.update(fruit_other_set)
# print(fruit_set)

# fruit_set = set({"papaya", "apple", "pear", "cherry", "orange"})
# fruit_other_set = set({"coconut", "papaya"})
# fruit_set.update(fruit_other_set)
# print(fruit_set)


# basket_a = {"apple", "banana", "cherry"}
# basket_b = {"banana", "cherry", "mango"}
# basket_c = set()
# basket_c.update(basket_a, basket_b)
# print(basket_c)
