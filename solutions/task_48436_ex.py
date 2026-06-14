# Student ID : 48436-ex
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the absolute difference between the sum of even digits and the sum of odd digits.║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_48436_ex.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    # Remove "-ex" suffix if present
    if id.endswith("-ex"):
        id = id[:-3]

    even_sum = 0
    odd_sum = 0

    for ch in id:
        if ch.isdigit():
            digit = int(ch)

            if digit % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit

    return abs(even_sum - odd_sum)



if __name__ == "__main__":
    print(solve("48436-ex"))
