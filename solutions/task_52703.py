# Student ID : 52703
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the minimum NON-ZERO digit in your ID.           ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52703.py


def solve(id: str) -> int:
    return min(int(x) for x in id if x.isdigit() and x != '0')
    pass


if __name__ == "__main__":
    print(solve("52703"))
