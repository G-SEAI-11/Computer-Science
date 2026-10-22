"""
You are given an array, paths, where each element paths[i] = [cityAᵢ, cityBᵢ] represents a direct route from cityAᵢ to cityBᵢ.
Your task is to identify the final city on the route — the one that has no outgoing path to any other city.
The structure of the routes is guaranteed to be a simple chain without loops, so there will be exactly one such destination.
https://leetcode.com/problems/destination-city/description/
"""

paths = [
    ["London", "New York"],
    ["Lima", "Sao Paulo"],
    ["New York", "Lima"],
]
# Output: "Sao Paulo"
#
# paths = [["B", "C"], ["D", "B"], ["C", "A"]]
# Output: "A"

# paths = [["A", "Z"]]
# Output: "Z"


# Standardansatz Setdifferenz: Welche Stadt unter den Zielen kommt nicht in den Starts vor?
def destCity(paths):  # O(n)
    starts = set()
    destinations = set()

    for a, b in paths:  # städte aufteilen - O(n)
        starts.add(a)  # Start stadt
        destinations.add(b)  # Ziel Stadt

    # Mengen-Differenz: destinations - starts liefert alle Elemente,
    # die in destinations vorkommen, aber nicht in starts.
    # Da es garantiert genau eine Endstadt gibt, enthält das Ergebnis-Set
    # nur ein Element — .pop() holt es heraus.
    return (destinations - starts).pop()


# Standardansatz Traversal: Liste in Dictionary umwandeln und von Start zu Zielen durchwandern
def destCity(paths):  # O(n) (Leicht ineffiziender als Setdifferenz)
    # paths ist eine Liste von [Start, Ziel]-Paaren.
    # dict(paths) wandelt sie direkt in ein Dictionary um:
    # {"London": "New York", "New York": "Lima", "Lima": "Sao Paulo"}
    # Jede Startstadt zeigt damit auf ihre nächste Zielstadt.
    destinations_map = dict(paths)  # O(n)

    # Wir starten an der Zielstadt des ersten Eintrags und reisen von dort weiter.
    curr_place = paths[0][1]

    # Solange die aktuelle Stadt selbst noch Startpunkt eines Pfades ist, weiterreisen.
    # Die Schleife endet, wenn curr_place nicht mehr als Schlüssel im Dictionary steht
    # → das ist die Endstation ohne ausgehenden Pfad.
    while curr_place in destinations_map:  # O(n)
        curr_place = destinations_map.get(curr_place)

    return curr_place


print(destCity(paths))


# cities = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

# dict_seen_cities_start = set()  # Speicher: O(n)
# dict_seen_cities_destination = set()  # Speicher: O(n)
# for start, end in cities:  # O(n) <-
# dict_seen_cities_start.add(start)
#     dict_seen_cities_destination.add(end)

# final_destination = (dict_seen_cities_destination - dict_seen_cities_start).pop()
# print(final_destination)


# set_starts = {"London"}
# set_ends = {"Sao Paulo"}


# def destination(routes):
#     abflug = {   stop[0] for stop in routes   } # O(n)
#     return [stop[1] for stop in routes if stop[1] not in abflug].pop()

# Testhack
# def destination_City1(route):
#     return route.pop().pop()


# [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

# routes = {"London": "New York", "New York": "Lima", "Lima": "Sao Paulo"}


# def destination_City2(travelroute):
#     routes = {}
#     start = ""
#     ziel = ""
#     for route in travelroute:
#         ziel = route[1]
#         start = route[0]
#         routes.update({start: ziel})
#         # print(routes)

#     # routes = dict(travelroute)

#     for route in travelroute:
#         ziel = route[1]
#         if ziel not in routes.keys():
#             # if ziel not in routes:
#             return ziel
#     return None


def finalcity(cities):
    # Startstädte sammeln = jeweils 1. Wert vom jeweiligen Index
    cityA = []
    for index in cities:  # O(n)
        cityA.append(index[0])
    # Endstädte sammeln = jeweils 2. Wert vom jeweiligen Index
    cityE = []
    for index in cities:
        cityE.append(index[1])
    # vergleichen ob die Endstädte auch in den Startstädten vorkommen
    for c in range(len(cityE)):  # O(n)
        if cityE[c] not in cityA:  # Wert nicht in Liste # O(n²)
            return cityE[c]


# -------------------------------------
# Tests
# -------------------------------------
cases = [
    (
        [[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]],
        "Sao Paulo",
    ),
    ([[["B", "C"], ["D", "B"], ["C", "A"]]], "A"),
    ([[["A", "Z"]]], "Z"),
]


def test(fn, cases):
    for input, expected in cases:
        output = fn(*input)
        try:
            assert output == expected
            print(f"Test succeeded: {input} -> {output}")
        except AssertionError:
            print(f"Test failed: expected {expected}, got {output}")


# test(destination, cases)
test(finalcity, cases)
