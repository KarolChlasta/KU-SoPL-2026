# Student ID : 52653
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the product of all NON-ZERO digits in your ID.   ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52653.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    result = 1
    for ch in id:
        if ch.isdigit() and ch != '0':
            result *= int(ch)
    return result


if __name__ == "__main__":
    print(solve("52653"))
