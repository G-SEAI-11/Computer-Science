# Eine Funktion wird mit def definiert. Der eingerückte Block wird erst beim
# Aufruf ausgeführt.
# Grundlegende Syntax:
# def sum_numb(num_a, num_b):
#     return num_a + num_b

# def funktionsname():
#     ausdruck


def say_hello():
    print("Hello")


print("Funktion wurde definiert")
# Die Funktion wurde bisher nur definiert. Jeder Aufruf startet den Block neu.
say_hello()
say_hello()
say_hello()

print()
print("Double a number")


def double_number(number):
    """Gibt das Doppelte der übergebenen Zahl zurück."""
    return number * 2


result = double_number(4)
# return beendet den Funktionsaufruf und liefert einen Wert an den Aufrufer.
print(result)
print(double_number(10))
print(result + 1)
# help(double_number)

print("3. output und return value")
# print zeigt etwas an, return liefert einen Wert. say_hello gibt hier None zurück.
display_result = say_hello()
print(display_result)

print("4. return from a branch")


def describe_number(number):
    # Jede Verzweigung muss einen Rückgabewert liefern, damit für jeden
    # möglichen Zahlenwert ein Ergebnis zurückgegeben wird.
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


tested_number = describe_number(22)
print(tested_number)

print("5. print inside a loop")


def show_numbers(count):
    # Eine Funktion kann auch direkt Ausgaben erzeugen, ohne eine Liste
    # zurückzugeben.
    for number in range(1, count + 1):
        print(number)


show_numbers(15)

print("6. return a list")


def double_numbers_list(numbers):
    # Das Ergebnis wird lokal aufgebaut und erst am Ende als neue Liste
    # zurückgegeben. Die Eingabeliste wird dabei nicht verändert.
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


print(double_numbers_list([1, 2, 3, 4, 5]))
print(double_numbers_list([]))
