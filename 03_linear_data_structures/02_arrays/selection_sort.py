# Zuerst die Position des kleinsten Werts finden.
values = [64, 25, 12, 22, 11]
minimum_index = 0

for index in range(1, len(values)):
    if values[index] < values[minimum_index]:
        minimum_index = index

print("Indexposition des Minimums:", minimum_index)
print("Wert des Minimums:", values[minimum_index])

# Den kleinsten Wert an der ersten Position platzieren.

selection_demo = values.copy()
selection_demo[0], selection_demo[minimum_index] = (
    selection_demo[minimum_index],
    selection_demo[0],
)
print(selection_demo)

# Nach jedem Durchlauf beginnt der unsortierte Bereich eine Position weiter rechts.


def selection_sort(numbers):
    # Eine Kopie sortieren, damit die ursprüngliche Liste unverändert bleibt.
    result = numbers.copy()

    for start in range(len(result) - 1):
        # Am Anfang des unsortierten Bereichs wird zunächst das Minimum vermutet.
        minimum_index = start

        # Die übrigen Werte des unsortierten Bereichs auf ein kleineres Minimum prüfen.
        for index in range(start + 1, len(result)):
            if result[index] < result[minimum_index]:
                minimum_index = index

        # Nur tauschen, wenn ein neues Minimum gefunden wurde.
        if minimum_index != start:
            result[start], result[minimum_index] = result[minimum_index], result[start]

    return result


print(selection_sort(values))
