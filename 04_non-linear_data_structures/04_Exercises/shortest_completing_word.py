# https://learn.wbscodingschool.com/courses/software-engineering/lessons/exercises-2/topic/%f0%9f%a7%a9-shortest-completing-word/

# Your task is to find the shortest word in words that completes the licensePlate.

# Variante 1


def ausgabewort(plate, wörter):
    # --- Schritt 1: Kennzeichen aufbereiten und Buchstaben zählen ---
    # Groß-/Kleinschreibung vereinheitlichen
    new_plate = plate.lower()
    # Dictionary (Hash Map) zum Zählen der benötigten Buchstaben anlegen
    buchstabenzähler = {}

    for c in new_plate:
        # Nur echte Buchstaben berücksichtigen (Zahlen und Leerzeichen ignorieren)
        if c.isalpha():
            if c in buchstabenzähler:
                buchstabenzähler[c] += 1
            else:
                buchstabenzähler[c] = 1

    # --- Schritt 2: Jedes Wort prüfen und das kürzeste gültige Wort merken ---
    kürzesteswort = None

    for wort in wörter:
        # Zunächst annehmen, dass das aktuelle Wort alle Buchstaben enthält
        wortpasst = True

        # Jeden benötigten Buchstaben samt seiner Mindestanzahl überprüfen
        for buchstabe, anzahl in buchstabenzähler.items():
            # Kommt der Buchstabe im Wort seltener vor als benötigt, fällt das Wort raus
            if wort.count(buchstabe) < anzahl:
                wortpasst = False
                break

        # Wenn das Wort alle Bedingungen erfüllt hat:
        if wortpasst == True:  # noqa: SIM102
            # Speichern, falls es der erste Treffer ist oder echt kürzer als der bisherige
            # (Durch '<' bleibt bei gleicher Länge automatisch das zuerst gefundene Wort erhalten)
            if kürzesteswort == None or len(wort) < len(kürzesteswort):
                kürzesteswort = wort

    # --- Schritt 3: Kürzestes passendes Wort zurückgeben ---
    return kürzesteswort


# * Example 1
# print("---1.---")
# licensePlate = "1s3 PSt"
# words = ["step", "steps", "stripe", "stepple"]
# # Output "steps"
# print(ausgabewort(licensePlate, words))
# # * Example 2
# print("---2.---")
# licensePlate = "1s3 456"
# words = ["looks", "pest", "stew", "show"]
# # Output "pest"
# print(ausgabewort(licensePlate, words))


# Variante 2


def _filter(licensplate: str) -> dict:
    # bereinigt Nummernschild von allem was nicht Buchstabe ist
    chars = licensplate.lower()
    chars_tmp = {}
    for char in chars:
        if char.isalpha():
            chars_tmp[char] = chars_tmp.get(char, 0) + 1
    # print(chars)
    return chars_tmp


def _is_valid_word(word, chars) -> bool:
    # prüft ob Nummernschild buchstaben in Wort vorkommen
    # und ob wort min mehr als die Anzahl
    # der im Nummernschild enthaltenen Buchstaben hat
    for char in chars:
        count = word.count(char)
        if count < chars[char]:
            return False
    return True


def find_word(plate: str, words: list) -> str:
    # Hauptfunktion
    chars = _filter(plate)
    print(chars)
    shortest = ""
    for word in words:
        word2test = word.lower()
        if _is_valid_word(word2test, chars) and (
            len(shortest) == 0 or len(word) < len(shortest)
        ):
            shortest = word
    return shortest


words = ["Wolfgang", "step", "stepple", "steps", "ste", "Stp", "stepple", "stripe"]
plate = "1s3 P5t"
print(find_word(plate, words))

words = ["step", "steps", "stripe", "stepple"]
plate = "1s3 PSt"
print(find_word(plate, words))

words = ["looks", "pest", "stew", "show"]
plate = "1s3 456"
print(find_word(plate, words))


# Variante 3


def letter_counts(text):
    # Zählt, wie oft jeder Buchstabe in einem Text vorkommt.
    counts = {}
    for character in text:
        if character.isalpha():  # Ziffern und Leerzeichen zählen nicht.
            # Alle Buchstaben werden in Kleinbuchstaben umgewandelt,
            # damit Groß- und Kleinschreibung keinen Unterschied macht.
            letter = character.lower()
            # Beim ersten Vorkommen beginnt der Zähler bei 0.
            counts[letter] = counts.get(letter, 0) + 1
    return counts


# Die benötigten Buchstaben des Kennzeichens einmal ermitteln.
required = letter_counts("1s3 PSt")
print("Required:", required)


def completes(word, required):
    # Prüft, ob ein Wort alle benötigten Buchstaben
    # mindestens so oft wie im Kennzeichen enthält.
    available = letter_counts(word)
    for letter, amount in required.items():
        # Ein fehlender Buchstabe zählt als 0. Ein einziger zu kleiner Vorrat reicht für False.
        if available.get(letter, 0) < amount:
            return False
    return True  # Erst hier sind alle benötigten Buchstaben geprüft.


print("step:", completes("step", required))
print("steps:", completes("steps", required))


def shortest_completing_word(license_plate, words):
    # Ermittelt zunächst die Buchstaben und ihre benötigten Häufigkeiten.
    required = letter_counts(license_plate)
    # None bedeutet, dass bisher noch kein passendes Wort gefunden wurde.
    shortest = None
    for word in words:
        # Nur Wörter berücksichtigen, die das Kennzeichen vervollständigen.
        if completes(word, required):  # noqa: SIM102
            # None steht für „noch kein Treffer“. Bei gleicher Länge bleibt der frühere Treffer.
            if shortest is None or len(word) < len(shortest):
                # Das erste passende Wort oder das bisher kürzeste Wort speichern.
                shortest = word
    return shortest


# Beispiel 1: "steps" ist das kürzeste Wort, das s und t enthält.
print(shortest_completing_word("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
# Beispiel 2: "pest" ist das kürzeste Wort, das s und t enthält.
print(shortest_completing_word("1s3 456", ["looks", "pest", "stew", "show"]))
