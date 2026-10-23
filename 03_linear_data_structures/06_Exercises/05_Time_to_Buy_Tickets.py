"""
There are n people lined up to buy tickets, with person 0 at the front and person n - 1 at the back.
You are given a 0-indexed array tickets of length n, where tickets[i] is the number of tickets person i wants to purchase.

Each ticket purchase takes exactly 1 second. Each person can only buy one ticket at a time.
If, after buying a ticket, a person still needs more tickets, they immediately move to the end of the line.
If a person no longer needs any tickets, they leave the line entirely.

You need to calculate how many seconds it takes for the person who starts at position k (0-indexed) to finish buying all of their tickets.
https://leetcode.com/problems/time-needed-to-buy-tickets/description/
"""

#
tickets = [2, 3, 2]
k = 2
# Output: 6

# tickets = [5, 1, 1, 1]
# k = 0
# Output: 8

from collections import deque


# Standardlösung 1 - Simulation mit Queue
def time_to_buy_tickets(
    tickets: list[int], k: int
) -> (
    int
):  # O(n * n[k]) -> Solang die Queue durchscannen, bis unser Hero alle Tickets gekauft hat.
    # Wir speichern jede Person als Tupel (Index, Anzahl benötigter Tickets) in einer Warteschlange.
    queue = deque((i, t) for i, t in enumerate(tickets))
    seconds = 0

    while queue:
        # Die Person ganz vorne kommt dran: popleft() entfernt das erste Element (FIFO-Prinzip).
        person, count = queue.popleft()
        seconds += 1
        count -= 1  # Eine Sekunde vergeht, die Person kauft 1 Ticket.

        # Wenn das die gesuchte Person k ist und sie keine Tickets mehr braucht, sind wir fertig.
        if person == k and count == 0:
            return seconds

        # Hat die Person noch Tickets übrig, stellt sie sich hinten wieder an.
        if count > 0:
            queue.append((person, count))

    return seconds


# Standardlösung 1b - Simulation mit Kreisförmige Indizierung
#  Ist ein wenig effizienter als mit Queue, aber immer noch müssen wir die Liste immer wieder durchscannen, bis unser Hero alle Tickets hat.
def timeRequiredToBuy(tickets: list[int], k: int) -> int:  # O(n * tickets[k])
    seconds = 0
    n = len(tickets)
    i = 0  # Index der aktuell an der Reihe seienden Person
    # Solange Person k noch Tickets braucht, läuft die Simulation.
    while tickets[k] > 0:
        if tickets[i] > 0:
            # Person i kauft ein Ticket — ihr Zähler wird um 1 reduziert.
            tickets[i] -= 1
            seconds += 1
            # Ziel erreicht: Person k hat alle Tickets gekauft.
            if tickets[k] == 0:
                return seconds
        # Modulo springt am Ende der Liste automatisch wieder zum Anfang — wie eine kreisförmige Schlange.
        i = (i + 1) % n

    return seconds


# Standardlösung 2 - Mathematisch
def timeRequiredToBuy(
    tickets: list[int], k: int
) -> int:  # O(n) - ein einzelner Scan durch die Liste
    # Statt zu simulieren, rechnen wir direkt aus, wie viele Sekunden vergehen.
    # Idee: Person k braucht genau tickets[k] Runden. Wir zählen, wie oft jede andere Person
    # in diesen Runden die Schlange blockiert.
    total = 0
    for index, value in enumerate(tickets):
        if index <= k:
            # Personen *vor* oder _an_ Position k sind in jeder der tickets[k] Runden noch dabei.
            # Sie können also höchstens tickets[k] mal kaufen (oder weniger, wenn ihr Vorrat kleiner ist).
            total += min(value, tickets[k])
        else:
            # Personen *hinter* k sind nur in tickets[k]-1 Runden dabei:
            # In der letzten Runde kauft Person k ihren letzten Ticket und verlässt vorher die Schlange,
            # bevor die Personen hinter ihr noch einmal drankommen.
            total += min(value, tickets[k] - 1)
    return total


# Wie Methode 1
def how_long_does_it_take_to_buy_alle_the_tickets(queue, start_position_in_line):
    waiting_time = 0
    customers = deque()  # mem: O(n)

    for pos, tickets_to_buy in enumerate(queue):  # O(n)
        print(pos, tickets_to_buy)
        customers.append(
            {"hero": pos == start_position_in_line, "tickets_to_buy": tickets_to_buy}
        )

        # [  { "hero": False, "tickets_to_buy": 3},  { "hero": True, "tickets_to_buy": 2}, ]

    hero_has_all_the_tickets = False

    while not hero_has_all_the_tickets:  # O(queue[k])
        customers[0]["tickets_to_buy"] -= 1
        waiting_time += 1
        if customers[0]["tickets_to_buy"] == 0:
            if customers[0]["hero"]:
                break
            customers.popleft()
        else:
            customers.append(customers.popleft())

    return waiting_time


# Wie Methode 1
def coast_time(ticket_list, index):  # O(n * ticket_list[index]))
    mensch_q = deque()
    for i in range(len(ticket_list)):  # o(n)
        mensch_q.append(i)

    timer = 0

    while mensch_q:  # O(ticket_list[index])
        curr = mensch_q.popleft()
        ticket_list[curr] = ticket_list[curr] - 1
        timer = timer + 1
        if curr == index and ticket_list[curr] == 0:
            return timer

        if ticket_list[curr] > 0:
            mensch_q.append(curr)


# Wie Methode 2
def timeToBuy(tickets, k):  # O(n)
    time = 0
    for i, number in enumerate(tickets):
        if i <= k:
            if number >= tickets[k]:
                time += tickets[k]
            else:
                time += number
        else:
            if number >= tickets[k]:
                time += tickets[k] - 1
            else:
                time += number
    return time


# -------------------------------------
# Tests
# -------------------------------------
cases = [
    (
        [[2, 3, 2], 2],
        6,
    ),
    ([[5, 1, 1, 1], 0], 8),
]


def test(fn, cases):
    for inp, expected in cases:
        output = fn(*inp)
        try:
            assert output == expected
            print(f"Test succeeded: {inp} -> {output}")
        except AssertionError:
            print(f"Test failed: expected {expected}, got {output}")


# test(how_long_does_it_take_to_buy_alle_the_tickets, cases)
test(timeToBuy, cases)
