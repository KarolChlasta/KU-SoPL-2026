# Student ID : 52588
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of squares of all digits in your ID.     ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52588.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    return sum(int(digit) ** 2 for digit in id if digit.isdigit())


if __name__ == "__main__":
    print(solve("52588"))
