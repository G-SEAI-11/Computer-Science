print("1. store function")


def square_number(number):
    return number * number


# Funktionen sind Werte. Die Zuweisung speichert die Funktion selbst, ohne sie
# aufzurufen. Deshalb stehen hier keine Klammern hinter square_number.
calculate = square_number  # Zuweisung ohne Parameterangaben
print(calculate(5))

print("2. function as argument")


def apply(operation, number):
    # operation ist eine Funktion und wird innerhalb von apply aufgerufen.
    return operation(number)


print(apply(square_number, 10))  # Funktion als Argument
print(apply(calculate, 10))

print("3. Store a function in a collection")
# Funktionen können wie andere Werte in Listen oder Dictionaries gespeichert werden.
operations = {"square": square_number}
selected_operation = operations["square"]
print(selected_operation(5))

print("4. Return a function")


def create_multiplier(factor):
    # multiply merkt sich den Wert factor aus dem äußeren Funktionsaufruf.
    def multiply(value):
        return value * factor

    return multiply


double = create_multiplier(2)
print(double(3))

print("5a. one expression")
# Lambda erzeugt eine kurze Funktion ohne eigenen def-Block und ohne return.
square = lambda value: value * value  # Lambda-Funktion
# Grundlegende Syntax:
# name = lambda parameter: expression
# Ein return ist nicht notwendig.

# Funktionsnamen nicht wiederverwenden:
# def square(value):
#     return value * value * value  # identisch zur Lambda-Funktion


# def square(value):
#     return value - 1
