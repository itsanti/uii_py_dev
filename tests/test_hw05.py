from divisor_master import *


def test_is_prime():
    assert is_prime(7), '7 is prime'
    assert not is_prime(6), '6 is not prime'


def test_get_divisors():
    assert get_divisors(7) == [1, 7]
    assert get_divisors(6) == [1, 2, 3, 6]


def test_get_max_prime_divisor():
    assert get_max_prime_divisor(1) is None
    assert get_max_prime_divisor(6) == 3
    assert get_max_prime_divisor(7) == 7
    assert get_max_prime_divisor(609840) == 11


def test_get_max_divisor():
    assert get_max_divisor(1) is None
    assert get_max_divisor(6) == 3
    assert get_max_divisor(7) == 1
    assert get_max_divisor(609840) == 304920


def test_canonical_decomposition():
    assert canonical_decomposition(7) == []
    assert canonical_decomposition(7, True) == 'prime number'
    assert canonical_decomposition(6) == [3, 2]
    assert canonical_decomposition(30) == [5, 3, 2]
    assert canonical_decomposition(30, True) == '2 * 3 * 5'
    assert canonical_decomposition(144) == [3, 3, 2, 2, 2, 2]
    assert canonical_decomposition(144, True) == '2 ^ 4 * 3 ^ 2'
