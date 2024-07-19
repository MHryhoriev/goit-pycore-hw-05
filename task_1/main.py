from typing import Callable

def main():
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))

def caching_fibonacci() -> Callable[[int], int]:
    """
    Creates a Fibonacci function with caching to improve performance.

    This function returns a nested `fibonacci` function that computes
    the Fibonacci number for a given integer `n` using a cache to store
    previously computed results.

    Returns:
        Callable[[int], int]: A Fibonacci function with caching.
    """
    cache = dict()

    def fibonacci(n: int) -> int:
        """
        Computes the Fibonacci number for a given integer `n` using caching.

        Args:
            n (int): The integer for which the Fibonacci number is to be computed.
                     Must be a non-negative integer.

        Returns:
            int: The Fibonacci number for the given integer `n`.
        """
        if n in cache:
            return cache[n]
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)

        cache[n] = result
        return result
    
    return fibonacci

if __name__ == "__main__":
    main()