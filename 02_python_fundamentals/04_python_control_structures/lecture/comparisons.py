print("--- 1. Minimum ---")
minutes = 45
minimum = 30
# >= prüft, ob der Wert mindestens so groß wie das Minimum ist.
print("Minimum reached?", minutes >= minimum)

print("--- 2. Boundary ---")
boundary_minutes = 30
# Die Grenze selbst ist nicht größer, aber sie ist mindestens erreicht.
print("Above minimum:", boundary_minutes > minimum)
print("Minimum reached:", boundary_minutes >= minimum)
# == prüft auf Gleichheit, != auf Ungleichheit.
print("Exactly minimum:", boundary_minutes == minimum)
print("Different from minimum:", boundary_minutes != minimum)


print("--- 3. and ---")
planned_minutes = 30
maximum = 90
has_minimum = planned_minutes >= minimum
within_maximum = planned_minutes <= maximum
# and ist nur dann True, wenn beide Bedingungen True sind.
print("Minimum reached:", has_minimum)
print("Within maximum:", within_maximum)
print("Valid duration:", has_minimum and within_maximum)

print("--- 4. or ---")
completed = False
# or ist True, sobald mindestens eine der beiden Bedingungen True ist.
print("Completed:", completed)
print("Minimum reached:", has_minimum)
print("Can finish?", completed or has_minimum)

print("--- 5. not ---")
needs_work = not completed and planned_minutes < maximum
# not kehrt den Wahrheitswert einer Bedingung um: False wird zu True.
print("Not completed:", not completed)
print("Needs work", needs_work)

print("--- 6. chained comparison ---")
topic = "Python"
# Eine leere Zeichenkette bedeutet, dass kein Thema vorhanden ist.
has_topic = topic != ""
print("Has topic?", has_topic)
# Verkettete Vergleiche prüfen beide Grenzen in einer einzigen Bedingung.
within_range = minimum <= planned_minutes <= maximum
print("Within range?", within_range)
print("Within range and has topic?", has_topic and within_range)
