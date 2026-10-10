
def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference of two numbers."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    return first * second


def divide(first: float, second: float) -> float:
    """Return the quotient of two numbers."""
    return first / second


def main() -> None:
    first = 10
    second = 5

    print(f"{first} + {second} = {add(first, second)}")
    print(f"{first} - {second} = {subtract(first, second)}")
    print(f"{first} * {second} = {multiply(first, second)}")
    print(f"{first} / {second} = {divide(first, second)}")


if __name__ == "__main__":
    main()