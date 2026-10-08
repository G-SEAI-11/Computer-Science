# def divide_10_by_n(number):
#     result = 10 / number
#     print(f"10 divided by {number} is {result}")


# divide_10_by_n("hi") #TypeError
# divide_10_by_n(0) #ZeroDivisionError
# divide_10_by_n(2)
# divide_10_by_n(3)


def divide_10_by_n(number):
    # Der riskante Ausdruck steht in try. Passende except-Blöcke behandeln
    # erwartbare Fehler, ohne dass das Programm an dieser Stelle abbricht.
    try:
        result = 10 / number
    except TypeError as error:
        print("That's not a valid number")
        print("Details:", error)
    except ZeroDivisionError:
        print("You can not divide by zero")
    else:  # Wird nur ausgeführt, wenn im try-Block kein Fehler auftrat.
        print(f"10 divided by {number} is {result}")
    finally:
        # Dieser Block läuft sowohl nach Erfolg als auch nach einem Fehler.
        print("the function ends here")


divide_10_by_n("hi")
# divide_10_by_n(0)
# divide_10_by_n(2)
