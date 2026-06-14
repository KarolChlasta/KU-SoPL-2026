# Student ID : 52620
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of all digits minus the maximum digit.   ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52620.py


def solve(id: str) -> int:
    digits = [int(ch) for ch in id if ch.isdigit()]
    return sum(digits) - max(digits)

if __name__ == "__main__":
    print(solve("52620"))  


if __name__ == "__main__":
    print(solve("52620"))
