print("--- 1. Sum of List Elements---")


def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_list([1, 2, 3, 4, 5]))

print("--- 2. Repeated Greeting ---")


def repeat_greeting(name, times):
    for nummer in range(times):
        print("Hallo", name)


repeat_greeting("Thomas", 3)

print("--- 3. Factorial Calculation ---")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 5
print(f"{n}! = {factorial(n)}")

print(factorial(5))
print(factorial(4))
print(factorial(0))
