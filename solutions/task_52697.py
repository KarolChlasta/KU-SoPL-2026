# Student ID : 52697
# Course : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║ YOUR TASK                                                ║
# ║                                                          ║
# ║ Return the sum of digits at EVEN positions (1-indexed:   ║
# ║ positions 1,3,5,...).                                    ║
# ║                                                          ║
# ║ - digits are extracted from your ID string               ║
# ║ - ignore the "-ex" suffix if present                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with: python task_52697.py

def solve(id: str) -> int:
    """
    Return the sum of digits at EVEN positions (1-indexed: 1, 3, 5, ...).
    Ignores the '-ex' suffix if present.
    """
    clean_id = id.replace("-ex", "").replace("_ex", "")
    digits = [ch for ch in clean_id if ch.isdigit()]
    return sum(int(digits[i]) for i in range(0, len(digits), 2))

if __name__ == "__main__":
    print(solve("52697"))
