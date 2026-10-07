print("--- 1. Starting condition ---")
studied_minutes = 0
goal_minutes = 90
print("More time needed:", studied_minutes < goal_minutes)

print("--- 2. Regular loop ----")
regular_minutes = 0
regular_goal = 90

# Die Bedingung wird vor jedem Durchlauf erneut geprüft.
while regular_minutes < regular_goal:
    # regular_minutes = regular_minutes + 30
    regular_minutes += 30
    print("Minutes:", regular_minutes)

print("After loop:", regular_minutes)

print("--- 3. Zero iterations ---")
zero_minutes = 0
zero_goal = 0

# Weil die Bedingung anfangs False ist, läuft der Schleifenrumpf kein einziges Mal.
while zero_minutes < zero_goal:
    zero_minutes += 30
    print("Minutes:", zero_minutes)
print("After loop:", zero_minutes)

print("--- 4. break ---")
break_minutes = 0
break_goal = 90

# break beendet die Schleife sofort, auch wenn die while-Bedingung noch True wäre.
while break_minutes < break_goal:
    break_minutes += 30
    if break_minutes == 60:
        break
    print("Minutes:", break_minutes)

print("After loop:", break_minutes)

print("--- 5. continue ----")
continue_minutes = 0
continue_goal = 90

while continue_minutes < continue_goal:
    continue_minutes += 30
    if continue_minutes == 60:
        continue  # nachfolgendes überspringen und zur Loopbedingung gehen
    print("Minutes:", continue_minutes)

print("After loop:", continue_minutes)

print("--- 6a. else after continue ---")

else_minutes = 0
else_goal = 90

# continue überspringt nur den Rest dieses Durchlaufs; die Schleife läuft weiter.
while else_minutes < else_goal:
    else_minutes += 30
    if else_minutes == 60:
        continue
    print("Minutes:", else_minutes)
else:  # noqa: PLW0120
    print("Goal reached without an early stop")
print("After loop", else_minutes)

print("--- 6b. else skipped by break ---")
break_else_minutes = 0
break_else_goal = 90

# Das else gehört zur Schleife und wird nach einem break nicht ausgeführt.
while break_else_minutes < break_else_goal:
    break_else_minutes += 30
    if break_else_minutes == 60:
        break
    print("Minutes:", break_else_minutes)
else:
    print("Goal reached without an early stop")

print("After loop", break_else_minutes)

print("--- 7. Running total ---")
current_number = 1
last_number = 4
running_total = 0

# Jeder Durchlauf addiert die aktuelle Zahl und erhöht anschließend den Zähler.
while current_number <= last_number:
    running_total = running_total + current_number
    # running_total += current_number
    current_number = current_number + 1
    # current_number += 1

print("Total", running_total)
