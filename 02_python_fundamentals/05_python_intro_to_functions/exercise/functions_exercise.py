print("--- 1. Sum of List Elements---")


def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_list([1, 2, 3, 4, 5]))
# Time Complexity of Big O Notation: O(n)

print("--- 2. Repeated Greeting ---")


def repeat_greeting(name, times):
    for nummer in range(times):
        print("Hallo", name)


repeat_greeting("Thomas", 3)
# Time Complexity of Big O Notation: O(n)

print("--- 3. Factorial Calculation ---")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Time Complexity of Big O Notation: O(n)

n = 5
print(f"{n}! = {factorial(n)}")

print(factorial(5))
print(factorial(4))
print(factorial(0))

print("--- 4. Fibonacci Sequence Generator ---")


def fibonacci(n):
    sequence = []

    for i in range(n):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


# Big O Notation:
# Time Complexity O(n)
# Space Complexity O(n)

print(fibonacci(7))
print(fibonacci(5))
print(fibonacci(1))
print(fibonacci(0))


def fibunacci(n):
    result = [0, 1]
    i = 0
    while i < n:
        result.append(result[-2] + result[-1])
        i += 1
    return result


print(fibunacci(10))


def fibenacci(n):
    start = [0, 1]
    for num in range(1, n):
        num = start[-1] + start[-2]
        start.append(num)
    print(start)


fibenacci(5)

print("5. Maximum of Two Numbers")


def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


print(max_of_two(5, 8))
print(max_of_two(10, 3))
print(max_of_two(4, 4))


def max_of_two_two(a, b):
    return f"{a} and {b} are the same number!" if a == b else (a if a > b else b)


print(max_of_two_two(6, 5))


def max_of_two_three(first_number, secend_number):
    if first_number > secend_number:
        print(f"{first_number} ist größer als {secend_number} !")
    elif first_number < secend_number:
        print(f"{secend_number} ist größer als {first_number} !")
    else:
        print("Beide Zahlen sind gleich groß")


max_of_two_three(3, 2)

# Big O Notation for Time Complexity O(1)


print("--- 6. Print a Pattern with Nested Loops ---")


def print_triangle(rows):
    colums = 0
    for i in range(rows):
        for j in range(colums):
            if j == 0 or i == rows - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        colums += 1
        print("*")


print_triangle(15)


def print_triangle_two(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()


# Big O Notation Time Complexity O(n^2)

print_triangle_two(8)


def print_triangle_three(rows):
    anzahl_sterne = 1
    y = rows * 4
    for row in range(2 * rows):
        print(("C " * anzahl_sterne).center(y, "."))
        anzahl_sterne += 1


print_triangle_three(5)


def print_triangle_four(rows):
    anzahl_sterne = 1
    y = rows * 4
    for row in range(2 * rows):
        print(("L " * anzahl_sterne).ljust(y, "."))
        anzahl_sterne += 1


print_triangle_four(5)

# Big O Notation Time Complexity: O(n^2)
