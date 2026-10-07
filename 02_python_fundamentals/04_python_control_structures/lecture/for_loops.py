print("--- 1. Topics ---")
topics = ["Conditions", "While", "For"]

# for besucht jedes Element der Liste genau einmal.
for topic in topics:
    print("Topic:", topic)
print("Topic loop finished")

print()
print("--- 2a. range(3)---")
# range(3) erzeugt die Werte 0, 1 und 2; das Ende ist ausgeschlossen.
for round_index in range(3):
    print("Round:", round_index)

print("--- 2b. range(1,4)---")
for another_index in range(1, 4):
    print("Round:", another_index)

print()
print("--- 3. break ---")
search_target = "While"
# break beendet die Suche beim ersten passenden Element.
for search_topic in topics:
    print("Checking:", search_topic)
    if search_topic == search_target:
        print("Found:", search_topic)
        break
print("Search finished")

print("---4. Skip with continue ---")
continue_target = "For"
# continue überspringt "While", ohne die Schleife vollständig zu beenden.
for continue_topic in topics:
    if continue_topic == "While":
        continue
    print("Checking:", continue_topic)
    if continue_topic == continue_target:
        print("Found:", continue_topic)
        break
print("Search finished")

print("---5a. Loop else with a match ---")
found_target = "For"
# Das Schleifen-else läuft nur, wenn kein break ausgeführt wurde.
for found_topic in topics:
    if found_topic == "While":
        continue
    print("Checking:", found_topic)
    if found_topic == found_target:
        print("Found:", found_target)
        break
else:
    print("Not found among checked topics")
print("Search finished")

print("---5b. Loop else without match ---")
found_target = "Case"
# Ohne Treffer erreicht die Schleife das else nach dem letzten Element.
for found_topic in topics:
    if found_topic == "While":
        continue
    print("Checking:", found_topic)
    if found_topic == found_target:
        print("Found:", found_target)
        break
else:
    print("Not found among checked topics")
print("Search finished")

print("--- 6. pass does not skip ---")
placeholder_target = "For"
# pass ist ein Platzhalter und überspringt nicht den restlichen Schleifenrumpf.
for placeholder_topic in topics:
    if placeholder_topic == "While":
        pass
    print("Checked:", placeholder_topic)
    if placeholder_target == placeholder_topic:
        break

print("--- 7. Nested loops ---")
days = ["Monday", "Tuesday", "Wednesday"]
# Die innere Schleife läuft für jeden Tag vollständig durch.
for day in days:
    for topic in topics:
        print(day, topic)

print("--- 8. search inside each topic---")
target_letter = "o"
# Die innere Schleife durchsucht jedes einzelne Zeichen des Themas.
for checked_topic in topics:
    print("Checked topic", checked_topic)
    for letter in checked_topic:
        if target_letter == letter:
            print("Found letter:", letter)
            break
    else:
        print("No letter found.")


print("--- 9. even round numbers ---")
# Der Modulo-Operator liefert bei geraden Zahlen den Rest 0.
for round_number in range(1, 7):
    if round_number % 2 == 0:
        print(round_number)
