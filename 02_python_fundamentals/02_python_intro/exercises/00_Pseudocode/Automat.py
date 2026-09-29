# * Die Mögliche Auswahl an Getränken
getraenke = {
    1: {"name": "Wasser", "preis": 1.0, "bestand": 10},
    2: {"name": "Cola", "preis": 1.5, "bestand": 5},
    3: {"name": "Saft", "preis": 2.0, "bestand": 0},
}

einwurf = 0.0
auswahl = int(input("Bitte wählen Sie ein Getränk (1-3)"))

# * Die Bestandsprüfung gibt die Bezahlung nur für ein verfügbares Getränk frei.
if getraenke[auswahl]["bestand"] > 0:
    einwurf = float(input(f"Bitte werfen Sie {getraenke[auswahl]['preis']} Euro ein: "))
    # * while prüft die Bedingung vor jedem Durchlauf erneut. Reicht der erste
    # * Einwurf bereits aus, wird der Schleifenblock vollständig übersprungen.
    while einwurf < getraenke[auswahl]["preis"]:
        print("Nicht genug Geld eingeworfen. Bitte werfen Sie mehr Geld ein.")
        # ! Weitere Einwürfe müssen die bisherige Summe erhöhen; mit = würde
        # ! nur der letzte Einwurf für die nächste Prüfung zählen.
        einwurf += float(
            input(
                f"Bitte werfen Sie {getraenke[auswahl]['preis'] - einwurf} Euro ein: "
            )
        )
    # * Außerhalb der Schleife, aber innerhalb des if-Blocks: Der Bestand sinkt
    # * genau einmal nach ausreichender Bezahlung, nicht bei jedem Einwurf.
    getraenke[auswahl]["bestand"] -= 1
else:
    # ! Die Aufforderung allein wiederholt die Auswahl nicht: Hier endet der Ablauf.
    print(
        f"Leider ist {getraenke[auswahl]['name']} ausverkauft. Bitte wählen Sie ein anderes Getränk."
    )
