# Student ID : 52627
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of digits greater than or equal to 6.    ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52627.py


def solve(id: str) -> int:
    total = 0
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """

    for digit in id:
        if digit.isdigit() and int(digit) >= 6:
            total += int(digit)

    return total


if __name__ == "__main__":
    print(solve("52627"))
