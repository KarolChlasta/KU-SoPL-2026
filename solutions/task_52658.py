# Student ID : 52658
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of digits at positions 2, 4, and 5 (1-indexed).║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52658.py

def solve(id: str) -> int:
    total = 0
    for digit in id:
        if int(digit) % 2 == 0:
            total += int(digit)
    return total

if _name_ == "_main_":
    print(solve("52658"))
