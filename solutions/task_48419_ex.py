# Student ID : 48419-ex
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
# Run with:  python task_48419_ex.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    product = 1

    for char in id:
        if char.isdigit() and char != "0":
            product = product * int(char)

    return product




if __name__ == "__main__":
    print(solve("48419-ex"))
