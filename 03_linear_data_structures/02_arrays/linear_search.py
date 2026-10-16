# Durchsucht die Werte von Anfang bis Ende nach dem Zielwert.
def linear_search(values, target):
    # enumerate liefert gleichzeitig den Index und den aktuellen Wert.
    for index, value in enumerate(values):
        # Sobald der Zielwert gefunden wurde, wird seine Position zurückgegeben.
        if value == target:
            return index

    # Wenn der Zielwert nicht vorkommt, gibt die Funktion -1 zurück.
    return -1


numbers = [4, 2, 7, 1, 8]
print(linear_search(numbers, 7))
# if linear_search(values, 1):
#    print("test")
