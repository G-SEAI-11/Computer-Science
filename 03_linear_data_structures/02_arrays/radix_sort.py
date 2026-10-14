def radix_sort(numbers):
    # Radix Sort verarbeitet hier nur nicht-negative Ganzzahlen.
    if any(number < 0 for number in numbers):
        raise ValueError("No negative numbers allowed.")

    # Eine leere Eingabe ist bereits sortiert.
    if not numbers:
        return []

    # Die Eingabe kopieren, damit die ursprüngliche Liste unverändert bleibt.
    result = numbers.copy()

    # Mit der Einerstelle beginnen und danach zur nächsten Stelle wechseln.
    exponent = 1
    maximum = max(result)

    # So lange wiederholen, wie der größte Wert an dieser Stelle noch eine Ziffer hat.
    while maximum // exponent > 0:
        # Je ein Bucket für die möglichen Ziffern 0 bis 9 anlegen.
        buckets = [[] for _ in range(10)]

        for number in result:
            # Die aktuelle Ziffer des Werts bestimmen.
            digit = (number // exponent) % 10

            # Den Wert in das Bucket seiner aktuellen Ziffer legen.
            # append erhält dabei die Reihenfolge innerhalb des Buckets.
            buckets[digit].append(number)

        # Die Buckets von 0 bis 9 wieder zusammenführen.
        result = [number for bucket in buckets for number in bucket]

        # In der nächsten Runde die nächsthöhere Stelle betrachten.
        exponent *= 10

    return result


values = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(values))
