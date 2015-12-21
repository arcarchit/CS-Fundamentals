Solving congruence equation
Python inherently supports long integers and its arithmetic
lambda expressions in python can work as c macros

Some Algorithms:

1) Trivial division (prime_factors.py)
We want to find factors of a number
All this factors would be a prime numbers.
In school days we used to find 'avibhajya avayavo'

Brute force way:
Keep incrementing divisor from 2 to n.
function name: factor1

Improvement:
If n has a factor, the factor can not be greater than sqrt(n)
Computing root is difficult, so we take a power of 2 for d
function name : factor2


2)Euclidian Algorithm (euclidian_algorithm.py)
we want to find gcd of a and b.
if b divides a then gcd = b
else
  a = qb + r
  now if some x divides a and b then from above equation it will also divide r.
  gcd (a, b) = gcd (b, r)
what if a< b:
  r = a % b = a
  gcd (a, b) = gcd (b, r) = gcd (b, a) so it gets swapped automatically.



3) Modular powers
We want to find ans = a^k % n
let k = 2*q + r
ans = (a ^ 2)^q * a ^ (0 or 1) % n
#r would be 0 or 1
#a ^ 2 is a * a
