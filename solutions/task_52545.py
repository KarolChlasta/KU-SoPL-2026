# Student ID : 52545
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of digits that are prime (2, 3, 5, or 7).║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52545.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.

    Returns the sum of digits in `id` that are prime (2, 3, 5, or 7).
    Non-digit characters (such as the "-ex" suffix) are ignored.
    """
    primes = {2, 3, 5, 7}
    return sum(int(ch) for ch in id if ch.isdigit() and int(ch) in primes)


if __name__ == "__main__":
    print(solve("52545"))
