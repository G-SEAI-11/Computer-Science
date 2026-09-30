print("--- String-Grundlagen ---")


# quote_example = "It's Python"
# print(quote_example)

# quote_example = 'He said "Hello"'
# print(quote_example)


# single_quotes = 'hello'
double_quotes = "World"
multi_line = """This is a
multi-line
string"""

print(multi_line)


greeting = "Hello" + " " + "Python"
print("Begrüßung:", greeting)

laugh = "ha" * 3
print("Lachen:", laugh)

print("--- Stringmethoden ---")

text = "  Hello Python World  "

print("Großbuchstaben:", text.upper())
print("Großbuchstaben:", text.lower())
print("Große Anfangsbuchstaben:", "hello python world".title())

print("[" + text.strip() + "]")
print("[" + text.lstrip() + "]")
print("[" + text.rstrip() + "]")

print(text.replace("Python", "JavaScript").strip())

print(text)

javascript_for_the_win = text.replace("Python", "JavaScript").strip()

words = text.strip().split()
print(words)

words = text.strip().upper()
print(words)


# text1 = "spam spam spam"

# parts = text1.split(" ")
# parts[2] = "eggs"
# text1 = " ".join(parts)
# print(text1)


print("'Python' in text:", "Python" in text)
print('"JavaScript" not in text:', "JavaScript" not in text)


print("-- Stringormatierung ---")

name = "Alice"
age = 25
gpa = 3.85

# print("My name is " + name + " and I am " + age + " years old.")
# print("My name is", name, "and I am", age, "years old.")
messagef = f"My name is {name} and I am {age} years old."
print("f-String:", messagef)

price = 3.1
print(f"Preis: {price:.2f} €")


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(itemno, quantity, price))
# print("My name is %s and I am %d years old." % (name, age))

print("--- Booleans und Wahrheitswerte ---")

is_sunny = True
is_raining = False

print("Sonnig:", is_sunny)
print("Regnerisch:", is_raining)

# truthy & falsy

# True
print(bool("Hello"))
print(bool(" "))
print(bool(42))
print(bool(-42))

# False
print(bool(""))
print(bool(0))
print(bool(None))


temperature = 25
is_warm = temperature > 20
print("Warm:", is_warm)


# * Zuweisungsoperatoren
x = 10
x += 5
# x = x + 5
print("Nach +=5:", x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print("Nach /=4:", x)

x //= 2
print("Nach //=2:", x)

x %= 2
print("Nach %=2:", x)

x = 2
x **= 3
# x = x**3
print("Nach **=3:", x)


print("--- Vergleichsoperatoren ---")

x = 10
y = 5

print(x == y)  # False
print(x != y)  # True
print(x > y)  # True
print(x < y)  # False
print(x >= 10)  # True
print(y <= 5)  # True

print("'apple' < 'banana':", "apple" < "banana")  # True
print("'Python' < 'python':", "Python" == "python")  # False
print("'z' < 'aa':", "z" < "aa")  # False
print("'a' < 'aa':", "a" < "aa")  # True

print("--- Logische Operatoren ---")

age = 10
has_license = True
can_drive = age >= 18 and has_license
print("Darf fahren:", can_drive)


is_weekend = False
is_holiday = True
can_relax = is_weekend or is_holiday
print("Kann entspannen:", can_relax)

is_raining = False
is_sunny = not is_raining

print("Sonnig:", is_sunny)


temperature = 25
is_summer = True
go_swimming = temperature > 20 and is_summer and not is_raining
print("Schwimmen gehen:", go_swimming)


# * Wir testen auf falsy & truthy
value = 0
print(value is not None)  # True
print(value != 0)  # False
print(not value)  # True


print("Länge:", len(text))
print(len("Hallo"))
print(len("ä"))
print(len("👍"))
print(len("👍🏽"))  # 2. Daumen + Hautfarbe

print("Anzahl von o:", text.count("o"))


sample = "Python lernen"
print(sample[0])
print(sample[-1])
print(sample[:6])

for char in sample:
    print(char)


scores = [10, 20]
same_scores = scores
other_score = [10, 20]

print(scores == other_score)  # Vergleichen den Inhalt
print(scores is same_scores)  # Vergleichen, ob es das selbe Objekt ist
print(scores is other_score)
print(scores is not other_score)
print(scores == other_score)
