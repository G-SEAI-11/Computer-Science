# Die Werte müssen aufsteigend sortiert sein.
def binary_search(values, target):
    # left und right markieren den aktuell betrachteten Suchbereich.
    left = 0
    right = len(values) - 1

    # Solange der Suchbereich nicht leer ist, wird weitergesucht.
    while left <= right:
        # Die Mitte teilt den Suchbereich in zwei Hälften.
        middle = (left + right) // 2
        value = values[middle]

        # Wenn der mittlere Wert das Ziel ist, wurde es gefunden.
        if value == target:
            return middle
        # Das Ziel kann nur in der rechten Hälfte liegen.
        if value < target:
            left = middle + 1
        # Das Ziel kann nur in der linken Hälfte liegen.
        else:
            right = middle - 1

    # Wenn der Suchbereich leer ist, wurde das Ziel nicht gefunden.
    return -1


numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(numbers, 4))
