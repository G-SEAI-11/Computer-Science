values = [12, 11, 13, 5, 6]


def insertion_sort(numbers):
    result = numbers.copy()  # ursprüngliche Liste wird nicht verändert

    for index in range(1, 5):  # 1, da der erste Wert sortiert ist
        current_value = result[index]
        position = index - 1  # vergleichen mit linken Nachbarn

        while position >= 0 and result[position] > current_value:
            result[position + 1] = result[
                position
            ]  # größeren Wert nach rechts schieben
            position -= 1  # Stelle (Index) weiter linsk prüfen

        result[position + 1] = current_value  # gemerkten Wert einsetzen

    return result


print(insertion_sort(values))
