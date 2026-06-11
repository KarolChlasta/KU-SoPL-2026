# Student ID : 52509
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of all NON-ZERO digits in your ID.       ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52509.py


def solve(id: str) -> int:
    return sum(int(d) for d in id if d.isdigit() and d != "0")
    

if __name__ == "__main__":
    print(solve("52509"))
