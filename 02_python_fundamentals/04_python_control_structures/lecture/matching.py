print("--- 1. Literal cases---")

command = "start"

# match vergleicht den Wert mit den Fällen von oben nach unten.
match command:
    case "start":
        print("Starting session")
    case "pause":
        print("Starting pause")
    case "stop":
        print("Stopping")
print("Command checked")

print("--- 2. Fallback ---")

unmatched_command = "restart"
# Der Unterstrich ist der Fallback für alle Werte ohne passenden Fall.
match unmatched_command:
    case "start":
        print("Starting session")
    case "pause":
        print("Starting pause")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
print("Command checked")

print("--- 3. Sequenze pattern ---")
result = ("completed", 75)

# Das Pattern zerlegt die Sequenz und bindet die zweite Position an minutes.
match result:
    case ("completed", minutes):
        print("Completed minutes:", minutes)
    case (status, _):
        print("Status:", status)
    case _:
        print("Unknown")

print("--- 4. Sequence with guard---")
guarded_result = ("completed", 75)

# Eine Guard-Bedingung verfeinert einen ansonsten passenden Fall.
match guarded_result:
    case ("completed", guarded_minutes) if guarded_minutes >= 60:
        print("Long completed session")
    case ("completed", guarded_minutes):
        print("Normal completed session")
    case (guarded_status, _):
        print("Status:", guarded_status)
    case _:
        print("Unknown")

print("--- 5a. type pattern and binding ---")

value = 75

# int() prüft den Typ und as bindet den Wert an eine neue Variable.
match value:
    case int() as number:
        print(number)
    case _:
        print("not an integer")


print("--- 5b. type pattern and binding ---")

guards_value = "-75"

# Guards erlauben zusätzliche Bedingungen, hier für positive und negative Zahlen.
match guards_value:
    case int() as positive_number if positive_number > 0:
        print("Positive number:", positive_number)
    case int() as negative_number if negative_number < 0:
        print("Negative number:", negative_number)
    case _:
        print("not an integer")
