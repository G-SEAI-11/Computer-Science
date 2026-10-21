# -------------------------------------
# Description
# -------------------------------------

# You're given a list of meeting intervals, where each interval is defined by a start time and an end time (intervals[i] = [startᵢ, endᵢ]).

# Determine whether it's possible for one person to attend every meeting without any overlaps.

# https://leetcode.com/problems/two-sum/submissions/1867469968/

# -------------------------------------
# Übung
# -------------------------------------

intervals = [[5, 10], [0, 30], [15, 20]]
# Output: False
# Explanation: Meeting [5,10] overlaps with [0,30], and [15,20] also overlaps with [0,30]

intervals2 = [[7, 10], [2, 4]]
# Output: True
# Explanation: [2,4] ends before [7,10] starts, so no overlap


# Standardlösung 1 Brute Force Ansatz — jedes Paar einzeln prüfen — O(n²)


# Hilfsfunktion: Prüft ob zwei Meetings i und j sich überlappen.
# Zwei Intervalle überlappen sich, wenn das eine startet, bevor das andere endet —
# egal welches der beiden früher beginnt.
def overlap(i, j):
    start_1, end_1 = i
    start_2, end_2 = j
    return (start_1 >= start_2 and start_1 < end_2) or (
        start_2 >= start_1 and start_2 < end_1
    )


def canAttendMeetings(intervals: list[list[int]]) -> bool:
    # Äußere Schleife: jedes Meeting einmal als "erstes" betrachten
    for i in range(len(intervals)):
        # Innere Schleife: nur Meetings nach i prüfen (bereits geprüfte Paare überspringen)
        # → Ergibt O(n²) Vergleiche insgesamt
        for j in range(i + 1, len(intervals)):
            if overlap(intervals[i], intervals[j]):
                return False

    return True


# Standardlösung 2: Sortieren + linearer Scan — O(n log n)
def canAttendMeetings(intervals: list[list[int]]) -> bool:

    # Nach Startzeit sortieren. Danach liegen sich überlappende Meetings
    # immer nebeneinander — wir müssen also nur benachbarte Paare prüfen.
    # Achtung! Mutiert die Originalliste!
    intervals.sort()

    # Jeden Meeting-Index ab dem zweiten durchlaufen
    for i in range(1, len(intervals)):
        # Überlappung: Das aktuelle Meeting startet, bevor das vorherige endet
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    # Kein Überlappung gefunden → alle Meetings können besucht werden
    return True


# Ansatz Set Intersectionen - An sich ist set() & set() sehr schnell ( O( mächtigkeit_kleineres_set ) )
# die termin_listen kännen aber sehr groß werden
# der erhöhte Speicherbedarf und die Erzeugung von Sets, die jeweils so groß sind, wie die einzelnen Intervalle, bringen diesen interessanten Ansatz unter die Performanz des Brute Force Ansatzes


def intersects(termine):
    termin_listen = []
    for termin in termine:
        termin_listen.append(list(range(termin[0], termin[1] + 1)))

    for index, termin in enumerate(termin_listen):
        for index_inner, termin_inner in enumerate(termin_listen):
            if index != index_inner and set(termin) & set(termin_inner):
                print("Intersected")
                return False
    return True


# Optimiert durch vorherige Sortierung -> O(n log n)
# Das ermöglicht einfahc immer das Ende eines Termins mit dem Anfang des nächsten Temins zu vergleichen

from collections import deque

termine = [[0, 30], [5, 10], [15, 20]]
termine = sorted(termine, key=lambda x: x[0])  # O(n log n)


class Queue:
    def __init__(self, liste):
        self.queue = deque(liste)

    def enque(self, item):
        self.queue.append(item)

    def deque(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def check_appointment_conflicts(self):  # O(n)
        while self.size() > 1:
            if self.deque()[1] > self.peek()[0]:
                return "Terminkonflikt"
        return "Kein Konflikt"


my_intervals = Queue(termine)
print(my_intervals.check_appointment_conflicts())


# ------------------------------------

# Gleicher Ansatz: Sortieren, Ende des Termins mit dem nächsten Anfang vergleichen


def meetings2(list_i):
    # list_i.sort()
    intervalle_sorted = sorted(list_i)  # O(n log n) <- Dominante Operation
    print(intervalle_sorted)

    for i in range(1, len(intervalle_sorted)):  # O(n)
        if (
            intervalle_sorted[i - 1][1] >= intervalle_sorted[i][0]
        ):  #  [[0, 30], [5, 10], [15, 20]]
            return False
    return True


termine = [[0, 30], [5, 10], [15, 20]]


# -------------------------------------
# Tests
# -------------------------------------
cases = [
    ([[[0, 30], [5, 10], [15, 20]]], False),
    ([[[7, 10], [2, 4]]], True),
]


def test(fn, cases):
    for input, expected in cases:
        output = fn(*input)
        try:
            assert output == expected
            print(f"Test succeeded: {input} -> {output}")
        except AssertionError:
            print(f"Test failed: expected {expected}, got {output}")


# test(can_attend_all, cases)

# test(canAttendMeetings, cases)


# test(intersects, cases)

# test(meetings2, cases)

test(canAttendMeetings, cases)
