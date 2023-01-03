from typing import Tuple, Iterator


def gcd(n: int, m: int) -> int:
    """
    Computes the GCD of two integers using
    the Euclidean algorithm.
    """

    while m:
        n, m = m, n % m

    return n


def egcd(n: int, m: int, depth=0) -> Tuple[int, int, int]:
    """
    Computes the GCD of two integers usiing
    the extended Euclidean algorithm.
    """

    if n == 0:
        return m, 0, 1
      
    gcd, u, v = egcd(m % n, n, depth+1)
    x = v - (m // n) * u
    y = u
    
    return gcd, x, y


def phi(n: int) -> int:
    """
    Computes the totative of an integer n.
    """

    totative = 0

    for m in range(1, n):
        totative += gcd(n, m) == 1

    return totative


def is_prime(n: int) -> bool:
    """
    Returns whether an integer is prime
    or not.
    """

    return phi(n) == n - 1


def primate_factors(n: int) -> Iterator[int]:
    """
    Computes the prime factorization of an
    integer.
    """

    m = 2

    while m ** 2 <= n:
        if not n % m:
            yield m
            n //= m

        else:
            m += 1

    if n > 1:
        yield n
