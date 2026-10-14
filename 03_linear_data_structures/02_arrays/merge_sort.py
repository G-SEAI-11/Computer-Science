def merge_sort(numbers):
    # Eine leere Liste oder eine Liste mit nur einem Element ist bereits sortiert.
    if len(numbers) <= 1:
        return numbers.copy()

    # Die Liste in zwei möglichst gleich große Hälften teilen.
    middle = len(numbers) // 2

    # Beide Hälften rekursiv sortieren.
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    # Die beiden sortierten Hälften wieder zu einer sortierten Liste verbinden.
    return merge(left, right)


def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    # Immer das jeweils kleinere Element der beiden Hälften übernehmen.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Eine Hälfte kann noch Elemente enthalten; sie sind bereits sortiert.
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


values = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(values))
