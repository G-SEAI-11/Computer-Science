def counting_sort(numbers):
    # Eine leere Eingabe ist bereits sortiert.
    if not numbers:
        return []

    # Kleinsten und größten Wert bestimmen, um den benötigten Wertebereich zu kennen.
    minimum = min(numbers)
    maximum = max(numbers)

    # +1, damit sowohl minimum als auch maximum enthalten sind.
    value_range = maximum - minimum + 1

    # Für jeden möglichen Wert einen Zähler mit dem Startwert 0 anlegen.
    counts = [0] * value_range

    for number in numbers:
        # Den Wert auf einen Index abbilden und sein Vorkommen zählen.
        # Die Verschiebung um minimum ermöglicht auch negative Zahlen.
        counts[number - minimum] += 1

    # Die sortierten Werte werden anhand ihrer Zähler neu aufgebaut.
    result = []

    for offset, count in enumerate(counts):
        # Die Verschiebung vom Array-Index zurück zum ursprünglichen Wert aufheben.
        value = offset + minimum

        # Den Wert so oft ergänzen, wie er in der Eingabe vorkam.
        result.extend([value] * count)

    return result


values = [4, 2, 2, 8, 3, 3, 1]  # LMS Beispiel
# values = [1, 2, 2, 2, 2, 100] # hohe Range
# values = [10001, 10002, 10003] # hohe Werte, kleine Range
print(counting_sort(values))
