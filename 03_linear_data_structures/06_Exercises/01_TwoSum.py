# -------------------------------------
# Description
# -------------------------------------

# You are given an array of integers, nums, and an integer, target.

# Your goal is to find indices of two distinct elements in nums whose sum equals target.

# You can't use the same element twice, and you may return the indices in any order.

# You can assume there is exactly one valid solution for each input.

# Follow-up: Can you come up with an algorithm that is less than O(n²) time complexity?

# https://leetcode.com/problems/two-sum/submissions/1867469968/

# -------------------------------------
# Übung
# -------------------------------------

nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]


def twoSum(arr: list[int], target: int):
    pass


# print(twoSum(nums, target))


# * Example 1:
# vorgegebene Zahlenliste
nummern = [2, 7, 11, 15]
# Zielzahl ist 9


def suche_result(nums, result):  # O(n)
    werte_index = {}
    for index, zahl in enumerate(nums):  # (0, 2), (1, 7)
        zahl_2 = result - zahl  # 9 - 2 = 7, 9 - 7 = 2
        if zahl_2 in werte_index:  # False ,
            # return f"{werte_index[zahl_2]} und {index}"
            return [werte_index[zahl_2], index]
        werte_index[zahl] = index  # {2: 0}


def two_sum_O2(nums, target):  # [2, 7, 11, 15]
    paare = [(num, index_ori) for index_ori, num in enumerate(nums)]
    paare.sort()  # [2, 7, 11, 15]
    # print("paare=", paare)
    # print("target=", target)
    # print(paare[0][0])

    if paare[0][0] >= 0:  # erster Wert
        # wenn der kleinste wert nicht neg,
        # dann können wir alle größeren Werte als
        # target eliminieren
        new_paare = []
        for paar in paare:
            # print(paar[0], "<", target, "?")
            if paar[0] <= target:
                new_paare.append(paar)
        paare = new_paare
    # weiter mit Additionsvergleich
    gefunden = False
    # print(paare)
    while len(paare) > 0 and not gefunden:
        sum_01 = paare.pop()
        # print(sum_01)
        for paar in paare:
            if sum_01[0] + paar[0] == target:
                sum_02 = paar
                gefunden = True
                break
    output = [sum_01[1], sum_02[1]]

    return output


def two_sum_On(nums, target):
    paare = [(num, index_ori) for index_ori, num in enumerate(nums)]
    paare.sort()

    li = 0
    re = len(paare) - 1
    gefunden = False

    while not gefunden and li != re:
        sum_01 = paare[li]
        sum_02 = paare[re]
        summe = sum_01[0] + sum_02[0]
        if summe == target:
            gefunden = True
            output = [sum_01[1], sum_02[1]]
            return output
        if summe > target:
            re -= 1
        else:
            li += 1
    return None


def sum_two(liste, target):  # O(n²)
    for index, value in enumerate(liste):
        for index_inner, value_inner in enumerate(liste):
            if index != index_inner and value + value_inner == target:
                return [index, index_inner]
    return "No Match"


def find_sum(list, target):

    n = len(list)

    for i in range(0, n - 1):

        # for j, value in enumerate(list):
        for j, value in enumerate(list):

            if i != j:
                if list[i] + list[j] == target:
                    print(f"index {i} + index {j} = {target}")
                    return


nums = [2, 7, 11, 13]


def twoSum(arr: list[int], target: int):  # O(n) - Linear
    # seen ist ein Dictionary: {Zahl -> Index}
    # Damit können wir in O(1) nachschlagen, ob eine bestimmte Zahl schon vorgekommen ist
    seen = {}  # O(1)

    for index, value in enumerate(arr):  # O(n) <- Dominante Operation
        # Welche Zahl fehlt uns noch, damit die Summe target ergibt?
        diff = target - value  # O(1)

        if diff in seen:  # O(1)
            # Die fehlende Zahl war schon in seen — wir haben das Paar gefunden
            return [seen[diff], index]
        else:
            # Noch kein Treffer — aktuelle Zahl mit Index für spätere Suchen merken
            seen[value] = index


# -------------------------------------
# Tests
# -------------------------------------
cases = [
    ([[2, 7, 11, 15], 9], [0, 1]),
    ([[3, 2, 4], 6], [1, 2]),
    ([[3, 3], 6], [0, 1]),
    ([[3, 2, 3], 6], [0, 2]),
]


def test(fn, cases):
    """
    Simple test utility function to verify if a function works correctly.

    Parameters:
    - fn: the function to test (e.g., twoSum)
    - cases: list of test cases, each containing (inputs, expected_output)
    """
    for input, expected in cases:
        # *input entpackt die Liste als einzelne Argumente — z.B. fn([2,7,11,15], 9)
        output = fn(*input)
        try:
            # assert wirft einen AssertionError, wenn die Bedingung False ist
            assert output == expected
            print(f"Test succeeded: {input} -> {output}")
        except AssertionError:
            print(f"Test failed: expected {expected}, got {output}")


# test(twoSum, cases)

# test(two_sum_O2, cases)
