values = [
    10,
    7,
    8,
    9,
    1,
    5,
    5,
]


def quick_sort(numbers):
    # Abbruch bei leerer Liste oder Liste mit 1 Element
    if len(numbers) <= 1:
        return numbers.copy()

    # Liste aufteilen in Teillisten (kleiner; gleich; größer)
    pivot = numbers[(len(numbers) // 2)]  # Abrunden bei Ganzzahldivision
    lower = [number for number in numbers if number < pivot]
    equal = [number for number in numbers if number == pivot]
    higher = [number for number in numbers if number > pivot]

    return quick_sort(lower) + equal + quick_sort(higher)


print(quick_sort(values))
