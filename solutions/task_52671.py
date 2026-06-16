# Student ID : 52671
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of the first 3 digits of your ID.        ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52671.py


def solve(id: str) -> int:
   def solve(id: str) -> int:
    digits = [int(c) for c in id if c.isdigit()]
    return sum(digits[:3])
    pass


if __name__ == "__main__":
    print(solve("52671"))
