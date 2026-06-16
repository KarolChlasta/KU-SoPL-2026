# Student ID : 52637
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
# Run with:  python task_52637.py


def solve(id: str) -> int:
    if id.endswith("-ex"):
        id = id[:-3]
    
    prime_digits = {'2', '3', '5', '7'}
    
    return sum(int(ch) for ch in id if ch in prime_digits)

if __name__ == "__main__":
    print(solve("52637"))