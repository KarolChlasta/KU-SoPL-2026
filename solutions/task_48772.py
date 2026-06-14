# Student ID : 48772
# Course     : Survey of Programming Languages — KU-SoPL-2026

def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    return sum(int(char) for char in id if char.isdigit())


if __name__ == "__main__":
    print(solve("48772"))
