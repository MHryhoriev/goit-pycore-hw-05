import re
from typing import Callable, Generator

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generates numbers found in the text.

    Args:
        text (str): The text to analyze.

    Yields:
        float: The numbers found in the text as floating point values.
    """
    pattern = r'\b\d+(?:\.\d{2})?\b'
    for price in re.findall(pattern, text):
        yield float(price)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the sum of numbers found in the text using a generator function.

    Args:
        text (str): The text to analyze.
        func (function): The generator function to extract numbers from the text.

    Returns:
        float: The sum of the numbers found.
    """
    return sum(func(text))

if __name__ == "__main__":
    main()