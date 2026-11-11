# Variante 2 von Manu
"""
PSEUDOCODE (BST from Preorder Traversal):

DENKWEISE A - Direktes Aufteilen der Liste (Teile & Herrsche):

FUNKTION BaueBSTAusPreorder(PreorderListe):

    1. SCHRITT - Basisfall (Abbruchbedingung):
    WENN PreorderListe leer ist:
        GIB None ZURÜCK

    2. SCHRITT - Wurzelknoten bestimmen:
    Nimm das erste Element der PreorderListe als WurzelWert
    Erstelle einen neuen Knoten (WurzelKnoten) mit diesem WurzelWert

    3. SCHRITT - Restliche Zahlen in Links und Rechts aufteilen:
    Sammle alle Zahlen aus PreorderListe, die KLEINER als WurzelWert sind, in einer LinkenListe
    Sammle alle Zahlen aus PreorderListe, die GRÖSSER als WurzelWert sind, in einer RechtenListe

    4. SCHRITT - Teilbäume rekursiv anhängen:
    Setze das linke Kind von WurzelKnoten auf das Ergebnis von BaueBSTAusPreorder(LinkeListe)
    Setze das rechte Kind von WurzelKnoten auf das Ergebnis von BaueBSTAusPreorder(RechteListe)

    5. SCHRITT - Fertigen Knoten liefern:
    GIB WurzelKnoten ZURÜCK


DENKWEISE B - Schrittweises Einfügen (wie beim normalen BST-Aufbau in bst.py):

FUNKTION BaueBSTÜberEinfügen(PreorderListe):

    1. SCHRITT - Startbaum anlegen:
    Lege einen leeren Suchbaum an (Wurzel ist anfangs None)

    2. SCHRITT - Alle Werte der Reihe nach einfügen:
    FÜR JEDEN Wert IN PreorderListe:
        Füge Wert nach der BST-Regel in den Baum ein:
            - Ist die aktuelle Stelle leer (None), erstelle dort einen neuen Knoten mit Wert
            - Ist Wert KLEINER als der aktuelle Knoten, gehe nach links weiter
            - Ist Wert GRÖSSER als der aktuelle Knoten, gehe nach rechts weiter

    3. SCHRITT - Wurzel zurückgeben:
    GIB die Wurzel des Suchbaums ZURÜCK


AUSGABE ALS LISTE (Etage für Etage mit Warteschlange / deque):

FUNKTION BaumZuListe(Wurzel):

    1. SCHRITT - Vorbereitung:
    Erstelle eine leere ErgebnisListe
    Erstelle eine Warteschlange (deque), in der zu Beginn nur Wurzel liegt

    2. SCHRITT - Baum Etage für Etage durchlaufen:
    SOLANGE Warteschlange nicht leer ist:
        Hole den vordersten Knoten aus der Warteschlange (.popleft())

        WENN Knoten gleich None ist:
            Hänge None an ErgebnisListe an
        SONST:
            Hänge Knoten.value an ErgebnisListe an
            Hänge Knoten.left hinten an Warteschlange an
            Hänge Knoten.right hinten an Warteschlange an

    3. SCHRITT - Überflüssige Nones am Ende abschneiden:
    SOLANGE das letzte Element in ErgebnisListe gleich None ist:
        Entferne das letzte Element (.pop())

    4. SCHRITT - Fertige Liste liefern:
    GIB ErgebnisListe ZURÜCK
"""

from collections import deque


# Knoten-Klasse für den binären Suchbaum
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None  # Linkes Kind (Werte kleiner als self.value)
        self.right = None  # Rechtes Kind (Werte größer als self.value)


# * Denkweise A: Direktes Aufteilen der Liste (Teile & Herrsche)


def BaueBSTAusPreorder(PreorderListe):
    # 1. Basisfall: Eine leere Liste ergibt keinen Knoten (None)
    if len(PreorderListe) == 0:
        return None

    # 2. Das erste Element der Preorder-Liste ist immer die aktuelle Wurzel
    wurzelwert = PreorderListe[0]
    wurzelknoten = BST(wurzelwert)

    # 3. Restliche Zahlen in kleinere (links) und größere (rechts) aufteilen
    linkeliste = []
    rechteliste = []
    for zahlen in PreorderListe:
        if zahlen < wurzelwert:
            linkeliste.append(zahlen)
        elif zahlen > wurzelwert:
            rechteliste.append(zahlen)

    # 4. Linken und rechten Teilbaum rekursiv aufbauen und anhängen
    wurzelknoten.left = BaueBSTAusPreorder(linkeliste)
    wurzelknoten.right = BaueBSTAusPreorder(rechteliste)

    # 5. Fertigen Wurzelknoten zurückgeben
    return wurzelknoten


# * Denkweise B: Schrittweises Einfügen nach der BST-Regel


def BaueBSTÜberEinfügen(PreorderListe):
    # Start mit einem leeren Baum
    wurzelknoten = None

    # Hilfsfunktion, die eine Zahl rekursiv an die passende freie Stelle setzt
    def hilfsfunktion(wurzelknoten, zahl):
        # Freie Stelle gefunden: Neuen Knoten mit der Zahl erstellen
        if wurzelknoten == None:
            return BST(zahl)
        # Kleinere Zahl wandert in den linken Teilbaum
        elif zahl < wurzelknoten.value:
            wurzelknoten.left = hilfsfunktion(wurzelknoten.left, zahl)
        # Größere Zahl wandert in den rechten Teilbaum
        elif zahl > wurzelknoten.value:
            wurzelknoten.right = hilfsfunktion(wurzelknoten.right, zahl)
        return wurzelknoten

    # Alle Zahlen der Preorder-Liste der Reihe nach in den Baum einfügen
    for zahl in PreorderListe:
        wurzelknoten = hilfsfunktion(wurzelknoten, zahl)
    return wurzelknoten


# * Funktion für die Etagen-Ausgabe im Terminal (Breitensuche / BFS mit Queue)
def BaumZuListe(Wurzel):
    printliste = []
    # Warteschlange startet mit dem Wurzelknoten
    warteschlange = deque([Wurzel])

    # Baum Etage für Etage von oben nach unten abarbeiten
    while len(warteschlange) > 0:
        knoten = warteschlange.popleft()
        if knoten is None:
            printliste.append(None)
        else:
            # Wert speichern und linkes sowie rechtes Kind hinten anstellen
            printliste.append(knoten.value)
            warteschlange.append(knoten.left)
            warteschlange.append(knoten.right)

    # Überflüssige None-Einträge ganz am Ende der Liste abschneiden
    while printliste[-1] is None:
        printliste.pop(-1)
    return printliste


# * Example 1
print("---1.---")
preorder = [8, 5, 1, 7, 10, 12]
# Output [8, 5, 10, 1, 7, None, 12]
baum = BaueBSTAusPreorder(preorder)
strauch = BaueBSTÜberEinfügen(preorder)
print(BaumZuListe(baum))
print(BaumZuListe(strauch))
# * Example 2
print("---2.---")
preorder = [1, 3]
# Output [1, None, 3]
baum = BaueBSTAusPreorder(preorder)
strauch = BaueBSTÜberEinfügen(preorder)
print(BaumZuListe(baum))
print(BaumZuListe(strauch))
