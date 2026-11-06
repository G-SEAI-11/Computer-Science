# * Variante 1: Naiver rekursiver Ansatz (ohne Zwischenspeicher)


# Zeitkomplexität: O(2^n) – viele Teilprobleme werden mehrfach berechnet.
# Speicherkomplexität: O(n) – maximale Rekursionstiefe des Aufrufstapels.
def berechneFibonacci(n):
    # Basisfälle (Abbruchbedingungen): F(0) = 0 und F(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        # Rekursiver Aufruf für die beiden vorherigen Positionen (n - 1) und (n - 2)
        ersterVor = berechneFibonacci(n - 1)
        zweiterVor = berechneFibonacci(n - 2)
        # Summe der beiden Vorgänger bilden und zurückgeben
        summeersterzweiter = ersterVor + zweiterVor
    return summeersterzweiter


# * Variante 2: Optimierter Ansatz mit Gedächtnis (Memoization / Dictionary)

# Zwischenspeicher (Notizzettel) mit den beiden bekannten Startwerten
speicher = {0: 0, 1: 1}


# Zeitkomplexität: O(n) – jede Fibonacci-Zahl wird höchstens einmal berechnet.
# Speicherkomplexität: O(n) – Dictionary und Rekursionsstapel wachsen linear.
def berechneFibonaccimitSpeicher(n):
    # 1. Prüfen, ob das Ergebnis für n bereits berechnet und gespeichert wurde
    if n in speicher:
        return speicher[n]
    else:
        # 2. Falls noch nicht im Speicher: einmalig aus den beiden Vorgängern berechnen
        summe_n_neu = berechneFibonaccimitSpeicher(
            n - 1
        ) + berechneFibonaccimitSpeicher(n - 2)
        # Neues Ergebnis für Position n im Dictionary merken
        speicher[n] = summe_n_neu
    # 3. Berechnetes Ergebnis zurückgeben
    return summe_n_neu


# * Example 1
print("---1.---")
n = 2
# Output 1
print(berechneFibonacci(2))
print(berechneFibonaccimitSpeicher(10))

# * Example 2
print("---2.---")
n = 3
# Output 2
print(berechneFibonacci(3))
print(berechneFibonaccimitSpeicher(20))
# * Example 3

print("---3.---")
n = 4
# Output 3
print(berechneFibonacci(4))
print(berechneFibonaccimitSpeicher(100))


# # --- Tuple unpacking
# #############################################
# # Zeitkomplexität: O(n) – eine Schleifeniteration pro Fibonacci-Position.
# # Speicherkomplexität: O(1) – nur zwei laufende Fibonacci-Werte.
# def fibonacci_3(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a


# print(fibonacci_3(10))


# # --- OOP
# #############################################
# class Triplet:
#     def __init__(self, value=1, vor=0, vorvor=1):
#         self.value = value
#         self.vor = vor
#         self.vorvor = vorvor


# class Fibo:
#     def __init__(self, root_value):
#         self.root = Triplet()
#         self.n = root_value

#     def _sum(self):
#         self.root.value = self.root.vor + self.root.vorvor
#         self.root.vorvor = self.root.vor
#         self.root.vor = self.root.value

# # Zeitkomplexität: O(n) – eine Iteration pro Fibonacci-Position.
# # Speicherkomplexität: O(1) – nur die drei Werte im Triplet.
#     def fibonacci_2(self):
#         for _ in range(self.n):
#             self._sum()
#         return self.root.value


# def fibonacci(n):
#     # Zeitkomplexität: O(2^n) – naive Rekursion mit mehrfachen Teilberechnungen.
#     # Speicherkomplexität: O(n) – maximale Rekursionstiefe.
#     if n == 0:
#         return 0
#     if n == 1:

#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def fibonacci2(n):
#     # Zeitkomplexität: O(n) – lineare Schleife von 2 bis n.
#     # Speicherkomplexität: O(1) – nur wenige Zwischenwerte.
#     if n == 0:
#         return 0
#     if n == 1:

#         return 1
#     else:
#         fib0 = 0
#         fib1 = 1
#         fib2 = 0
#         for i in range(2, n + 1):
#             fib2 = fib0 + fib1
#             fib0 = fib1
#             fib1 = fib2

#     return fib2

# print(fibonacci(4))
# print(fibonacci2(4))


# # Zeitkomplexität: O(n) – jede Fibonacci-Position wird einmal berechnet.
# # Speicherkomplexität: O(n) – das Dictionary speichert alle Ergebnisse.
# def fibonacci(n: int):
#     fibos = {0: 0, 1: 1}
#     for y in range(2, n + 1):
#         fibos[y] = fibos[y - 1] + fibos[y - 2]
#     return fibos[n], fibos[8]

# print(fibonacci(10))


# --- Matrix-Exponentiation (O(log n))
#############################################
# # Zeitkomplexität: O(log n) – binäres Potenzieren reduziert den Exponenten
# # bei jeder Iteration ungefähr auf die Hälfte.
# # Speicherkomplexität: O(1) – nur konstant viele 2x2-Matrizen.
# def fibonacci_4(n: int):
#     if n == 0:
#         return 0

#     # 2x2 Matrix-Multiplikation als Hilfsfunktion
#     def multiply_2x2(A, B):
#         return [
#             [
#                 A[0][0] * B[0][0] + A[0][1] * B[1][0],
#                 A[0][0] * B[0][1] + A[0][1] * B[1][1],
#             ],
#             [
#                 A[1][0] * B[0][0] + A[1][1] * B[1][0],
#                 A[1][0] * B[0][1] + A[1][1] * B[1][1],
#             ],
#         ]

#     # Einheitsmatrix I und Fibonacci-Basismatrix M
#     result = [[1, 0], [0, 1]]
#     base = [[1, 1], [1, 0]]

#     # Schnelles Potenzieren (Binary Exponentiation) in O(log n)
#     power = n
#     while power > 0:
#         if power % 2 == 1:
#             result = multiply_2x2(result, base)
#         base = multiply_2x2(base, base)
#         power //= 2

#     # result = [[F_(n+1), F_n], [F_n, F_(n-1)]]
#     return result[0][1]


# print(fibonacci_4(1000))
