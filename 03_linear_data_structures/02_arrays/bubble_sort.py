values = [5, 1, 4, 2, 8]

# Nur ein Nachbarpaar vergleichen und bei Bedarf tauschen.

pair_demo = values.copy()
if pair_demo[0] > pair_demo[1]:
    pair_demo[0], pair_demo[1] = pair_demo[1], pair_demo[0]

# Diese Schreibweise würde lediglich die gleichen Werte erneut zuweisen.
print(pair_demo)

# Ein Tausch mit einer zusätzlichen Variablen würde ebenfalls funktionieren:
# if pair_demo[0] > pair_demo[1]:
#     temp = pair_demo[0]
#     pair_demo[0] = pair_demo[1]
#     pair_demo[1] = temp

# Einen vollständigen Durchlauf über alle benachbarten Paare durchführen.

pass_demo = values.copy()

# len(pass_demo) ist 5. Die Indizes reichen von 0 bis 4.
# Da jeder Index mit dem darauffolgenden Index verglichen wird,
# würde ein Vergleich ab Index 4 zu einem IndexError führen.
# Deshalb endet der Bereich bei len(pass_demo) - 1.
for index in range(len(pass_demo) - 1):
    if pass_demo[index] > pass_demo[index + 1]:
        pass_demo[index], pass_demo[index + 1] = pass_demo[index + 1], pass_demo[index]

print(pass_demo)


def bubble_sort_basic(numbers):
    # Eine Kopie sortieren, damit die ursprüngliche Liste unverändert bleibt.
    result = numbers.copy()
    n = len(result)

    for pass_index in range(n - 1):
        swapped = False
        last_comparison = n - pass_index - 1
        # Das bereits sortierte Ende der Liste nicht erneut vergleichen.
        for index in range(last_comparison):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        # Wenn kein Tausch stattfand, ist die Liste bereits sortiert.
        if not swapped:
            break
    return result


print(bubble_sort_basic(values))
