def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    digits = []

    for char in id:
        if char.isdigit():
            digits.append(char)

    result = 0

    for digit in digits:
        if digits.count(digit) > 1:
            result += int(digit)

    return result


if __name__ == "__main__":
    print(solve("52633"))