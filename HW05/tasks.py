import divisor_master as dm

for i in range(11, 23):
    print(f'i={i:2}, is_prime={dm.is_prime(i):1}, max_prime_divisor={dm.get_max_prime_divisor(i)} ', end='')
    print(f'max_divisor={dm.get_max_divisor(i)}')
    print(f'    divisors={dm.get_divisors(i)}')
    print(f'    canonical decomposition={dm.canonical_decomposition(i, True)}')

'''OUT
i=11, is_prime=1, max_prime_divisor=11 max_divisor=1
    divisors=[1, 11]
    canonical decomposition=prime number
i=12, is_prime=0, max_prime_divisor=3 max_divisor=6
    divisors=[1, 2, 3, 4, 6, 12]
    canonical decomposition=2 ^ 2 * 3
i=13, is_prime=1, max_prime_divisor=13 max_divisor=1
    divisors=[1, 13]
    canonical decomposition=prime number
i=14, is_prime=0, max_prime_divisor=7 max_divisor=7
    divisors=[1, 2, 7, 14]
    canonical decomposition=2 * 7
i=15, is_prime=0, max_prime_divisor=5 max_divisor=5
    divisors=[1, 3, 5, 15]
    canonical decomposition=3 * 5
i=16, is_prime=0, max_prime_divisor=2 max_divisor=8
    divisors=[1, 2, 4, 8, 16]
    canonical decomposition=2 ^ 4
i=17, is_prime=1, max_prime_divisor=17 max_divisor=1
    divisors=[1, 17]
    canonical decomposition=prime number
i=18, is_prime=0, max_prime_divisor=3 max_divisor=9
    divisors=[1, 2, 3, 6, 9, 18]
    canonical decomposition=2 * 3 ^ 2
i=19, is_prime=1, max_prime_divisor=19 max_divisor=1
    divisors=[1, 19]
    canonical decomposition=prime number
i=20, is_prime=0, max_prime_divisor=5 max_divisor=10
    divisors=[1, 2, 4, 5, 10, 20]
    canonical decomposition=2 ^ 2 * 5
i=21, is_prime=0, max_prime_divisor=7 max_divisor=7
    divisors=[1, 3, 7, 21]
    canonical decomposition=3 * 7
i=22, is_prime=0, max_prime_divisor=11 max_divisor=11
    divisors=[1, 2, 11, 22]
    canonical decomposition=2 * 11
'''
