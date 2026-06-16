# Student ID : 52453
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of the first 2 digits minus the sum of the last 2 digits.║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52453.py


def solve(id: str) -> int:
    digits = [ch for ch in id.split("-")[0] if ch.isdigit()]
    first_two = int(digits[0]) + int(digits[1])
    last_two  = int(digits[-1]) + int(digits[-2])
    return first_two - last_two


if __name__ == "__main__":
    print(solve("52453"))
