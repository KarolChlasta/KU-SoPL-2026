# Student ID : 52561
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the digital root (repeatedly sum digits until single digit).║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52561.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    n = sum(int(ch) for ch in id if ch.isdigit())
    while n >= 10:
        n = sum(int(ch) for ch in str(n))
    return n

if __name__ == "__main__":
    print(solve("52561"))
