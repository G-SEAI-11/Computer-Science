# https://learn.wbscodingschool.com/courses/software-engineering/lessons/exercises-2/topic/%f0%9f%a7%a9-words-from-same-keyboard-row/
# Ein Wort darf nur Buchstaben aus genau einer Tastaturzeile enthalten.
# Die Zeilen werden als Zeichenketten beschrieben und später je nach Variante
# in Mengen oder direkt als Zeichenfolgen verwendet.

# First row: "qwertyuiop"
# Second row: "asdfghjkl"
# Third row: "zxcvbnm"

# Variante 1


def find_words(words):
    # Mengen erlauben mit issubset eine kompakte Prüfung:
    # Alle unterschiedlichen Buchstaben des Wortes müssen in einer Zeile liegen.
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = []
    for word in words:
        letters = set(word.lower())
        # lower() macht die Prüfung unabhängig von Groß- und Kleinschreibung.
        if letters.issubset(row1) or letters.issubset(row2) or letters.issubset(row3):
            result.append(word)
    return result


words = ["Hello", "Alaska", "Dad", "Peace"]

print(find_words(words))

# Variante 2


def _in_row(word: str, row: set) -> bool:  # subset
    # Durch die Umwandlung in eine Menge werden doppelte Buchstaben nur einmal
    # betrachtet; für die Zugehörigkeitsprüfung reicht das vollständig aus.
    test_word = set(word.lower())
    return test_word.issubset(row)


def _in_row2(word: str, row: set) -> bool:  # wort durchiterieren
    # Diese Variante prüft die Buchstaben nacheinander und kann beim ersten
    # ungültigen Zeichen sofort abbrechen.
    for char in word.lower():
        if char not in row:
            return False
    return True


def keyboard_rows() -> list:
    # Die Rückgabe als Liste von Mengen macht die Zeilen für die Suchfunktionen
    # wiederverwendbar und ermöglicht schnelle Mitgliedschaftsprüfungen.
    first_row = "qwertyuiop"
    second_row = "asdfghjkl"
    third_row = "zxcvbnm"

    first_row = set(first_row)
    second_row = set(second_row)
    third_row = set(third_row)

    return [first_row, second_row, third_row]


def search_for_words_in_row(words: list, rows: list) -> list:
    # Ein Wort wird für jede Zeile geprüft. Ist es in einer Zeile gültig,
    # wird es aufgenommen; die Daten enthalten hier keine doppelten Wörter.
    # Die verschachtelte List-Comprehension bildet diese beiden Schleifen ab.
    trusted_words = [word for word in words for row in rows if _in_row2(word, row)]
    return trusted_words


rows = keyboard_rows()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(search_for_words_in_row(words, rows))

# Variante 3


def keyboard(words):
    # Variante 3 verwendet Mengenliterale direkt und prüft jede Zeile einzeln.
    erste_zeile = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
    zweite_zeile = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
    dritte_zeile = {"z", "x", "c", "v", "b", "n", "m"}
    ergibniss = []

    for word in words:
        word_set = set(word.lower())
        # Die zusätzlichen Negationen stellen sicher, dass ein Wort nur in
        # der passenden Zeile landet und nicht mehrfach ergänzt wird.
        if word_set <= erste_zeile and not (
            word_set <= zweite_zeile or word_set <= dritte_zeile
        ):
            ergibniss.append(word)
        if word_set <= zweite_zeile and not (
            word_set <= erste_zeile or word_set <= dritte_zeile
        ):
            ergibniss.append(word)
        if word_set <= dritte_zeile and not (
            word_set <= erste_zeile or word_set <= zweite_zeile
        ):

            ergibniss.append(word)

    return ergibniss


words = ["Hello", "Alaska", "Dad", "Peace", "adsdf", "sfd"]
word1 = ["omk"]
print(keyboard(words))
print(keyboard(word1))


# Variante 4


def findWords(words):
    # Statt Mengen zu verwenden, wird jedes Zeichen direkt in der
    # entsprechenden Zeilenzeichenkette gesucht.
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    result = []

    for word in words:
        word_lower = word.lower()

        for row in rows:
            # all() liefert nur dann True, wenn jeder Buchstabe in der Zeile
            # vorkommt. Nach einem Treffer sind weitere Zeilen nicht nötig.
            if all(letter in row for letter in word_lower):
                result.append(word)
                break

    return result


words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))
