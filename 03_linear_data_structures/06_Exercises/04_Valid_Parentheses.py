"""
You have a string s composed only of the characters (, ), {, }, [ and ]. Determine if the bracket arrangement in this string is valid. Specifically, a valid string must meet the following criteria:

Each opening bracket has a corresponding closing bracket of the same type.
Brackets are closed in the correct order.
Every closing bracket matches an earlier opening bracket of the same type.
https://leetcode.com/problems/valid-parentheses/description/
"""

s = "([])"
# Out: True
#
# s = "([)]"
# Out: False

# s = "]"
# Out: False


# Standardansatz Stack mit Klammer-Lookup:
# Wenn ich eine schließende Klammer sehe, habe ich auch ihr Gegenstück als letztes gesehen?
def isValid(s):  # O(n)
    stack = (
        []
    )  # Zusätzlicher Speicherbedarf: O(n) - im schlimmsten Fall wird der Stapel so groß wie s

    #  Dictionary: jede schließende Klammer zeigt auf ihre passende öffnende
    parens_map = {")": "(", "]": "[", "}": "{", ">": "<"}

    for char in s:  # O(n) <- Dominante Operation
        if char in parens_map:  # ist schließende Klammer
            # habe ich schon die passende öffende Klammer gesehen?
            if len(stack) > 0 and stack[-1] == parens_map.get(char):
                stack.pop()  # vom Stapel nehmen - O(1)
            else:
                return False  # wir haben einen Syntaxfehler
        else:  # ist öffnende Klammer
            stack.append(
                char
            )  # Klammerpaar wurde geöffnet, muss wieder geschlossen werden - O(1)

    # Am Ende muss der Stack leer sein — sonst gibt es ungeschlossene Klammer
    return len(stack) == 0


# print(isValid(s))


# class Stack:
#     def __init__(self):
#         self.opening = None
#         self.allowed_brackets = {"(": ")", "[": "]", "{": "}"}
#         self.to_close_stack = []

#     def check_if_allowed(self, input_string):
#         for char in input_string:
#             if char in self.allowed_brackets:  # ist öffende Klammer?
#                 self.push(self.allowed_brackets[char])
#             # Wenn ich ein Closing Bracket habe, muss ich schauen, ob es gerade das erlaubte Closing Bracket ist
#             elif char in self.allowed_brackets.values():  # ist schließende klammer?
#                 if char == self.peek():
#                     self.to_close_stack.pop()
#                 else:
#                     return False
#         # Klammern müssen geschlossen werden, also muss der stack leer sein
#         return self.is_empty()  # '(((('

#     def push(self, char):
#         self.to_close_stack.append(char)

#     def peek(self):
#         return self.to_close_stack[-1]

#     def is_empty(self):
#         return len(self.to_close_stack) == 0


# checker = Stack()
# print(checker.check_if_allowed("([})"))


# -------------------------------------
# Tests
# -------------------------------------
cases = [
    (
        ["([])"],
        True,  # verschachtelt, aber korrekt geschlossen
    ),
    (["([)]"], False),  # falsche Reihenfolge beim Schließen
    (["]"], False),  # schließende Klammer ohne öffnende
]


def test(fn, cases):
    for inp, expected in cases:
        output = fn(*inp)
        try:
            assert output == expected
            print(f"Test succeeded: {inp} -> {output}")
        except AssertionError:
            print(f"Test failed: expected {expected}, got {output}")


test(isValid, cases)
