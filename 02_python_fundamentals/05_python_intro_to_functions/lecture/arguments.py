print("1. positional arguments")


def greet(name, greeting):
    return f"{greeting}, {name}"


# Positionsargumente werden anhand ihrer Reihenfolge den Parametern zugeordnet.
print(greet("Ada", "Hello"))
print(greet("Hello", "Ada"))
# greet("Ada", "Hello", "test")  # Ein Argument zu viel verursacht einen TypeError.

print("2. keyword arguments")
# Bei Keyword-Argumenten wird der Parametername explizit angegeben. Dadurch
# darf die Reihenfolge der Argumente geändert werden.
print(greet("Ada", greeting="Hello"))
print(greet(greeting="Hello", name="Ada"))

print("3. default value")


def greet_default(name, greeting="Hello"):
    return f"{greeting}, {name}"


# Fehlt greeting beim Aufruf, wird der Standardwert "Hello" verwendet.
print(greet_default("Ada"))

print("4. positional arguments")


def collect_numbers(*numbers):  # *args
    # * sammelt beliebig viele Positionsargumente in einem Tupel.
    print(type(numbers))
    return numbers


print(collect_numbers(1, 2, 3, 4, 5))

print("5. keyword arguments")


def collect_named(**values):
    # ** sammelt beliebig viele Keyword-Argumente in einem Dictionary.
    print(type(values))
    return values


print(collect_named(first=1, second=2))


print("6. restrictions")

# Vor / dürfen Argumente nur per Position übergeben werden.
# Nach * dürfen Argumente nur per Namen übergeben werden.


def add(first, second, /):
    return first + second


# print(add(first=2, second=3))  # Erzeugt einen TypeError.


def double(*, number):
    return number * 2


print(double(number=2))

# kombiniert
# def multiply(number, /, *, factor=2):
#     return number * factor
