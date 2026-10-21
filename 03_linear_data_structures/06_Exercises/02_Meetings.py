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


def canAttendMeetings(intervals):
    pass


print(canAttendMeetings(intervals))


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


def meetings2(list_i):
    # list_i.sort()
    intervalle_sorted = sorted(list_i)  # O(n log n) <-
    print(intervalle_sorted)

    for i in range(1, len(intervalle_sorted)):  # O(n)
        if (
            intervalle_sorted[i - 1][1] >= intervalle_sorted[i][0]
        ):  #  [[0, 30], [5, 10], [15, 20]]
            return False
    return True


termine = [[0, 30], [5, 10], [15, 20]]


def overlap(i, j):
    start_1, end_1 = i
    start_2, end_2 = j
    return (start_1 >= start_2 and start_1 < end_2) or (
        start_2 >= start_1 and start_2 < end_1
    )


def canAttendMeetings(intervals):
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if overlap(intervals[i], intervals[j]):
                return False
    return True


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
