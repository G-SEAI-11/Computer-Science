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

test(canAttendMeetings, cases)
