print("--- 1. if - true ---")
score = 94

if score >= 90:
    print("Grade A")

print("Evaluation complete")


print("--- 2. if - false ---")
lower_score = 84

if lower_score >= 90:
    print("Grade A")

print("Evaluation complete")

print("--- 3. if and else ---")
review_score = 84

if review_score >= 90:
    print("Grade: A")
else:
    print("Grade: needs review")
print("Evaluation complete")

print("--- 4. elif ---")
rating_score = 84
# Die Bedingungen werden von oben nach unten geprüft; der erste Treffer gewinnt.
if rating_score >= 90:
    print("Grade A")
elif rating_score >= 80:
    print("Grade B")
elif rating_score >= 70:
    print("Grade C")
else:
    print("Grade: needs review")

print("Evaluation complete")

print("--- 5. Store the grade ---")
stored_score = 84
# Die Variable grade erhält in jedem möglichen Fall einen Wert.
if stored_score >= 90:
    grade = "A"
elif stored_score >= 80:
    grade = "B"
elif stored_score >= 70:
    grade = "C"
else:
    grade = "Needs review"

print("Grade:", grade)
print("Evaluation complete")

print("--- 6a. Status with blocks ---")
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"
print("Status", status)

print("--- 6b. Conditional expression ---")
compact_age = 20
# die kurze Schreibweise nennt man auch
# ternary operator
compact_status = "adult" if compact_age >= 18 else "minor"
print("Status:", compact_status)
