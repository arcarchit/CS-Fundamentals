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


==============================

congruence : a is congruent to b modulo n
(a mod n) = (b mod n)
This also means n | (a-b)

Euper phi functions
Computes no of coprimes for a given number that are less than given number
euler_phi(20) =  8
list contains {1, 3, 7, 9, 11, 13, 17, 19}


RSA:
public key : encrypts the message
private key : decrypts the message

RSA procedure :
take p, q two prime numbers
n = pq
phi = euler_phi(n)
gcd(e, phi) = 1
d congruence e modulo (phi)
public key = (n, e)
private key = (p, q, d)
message = m
encrypt c congruence (m raised to e) (mode n) [m should b less than n]
decrypt c using m congruence (c raised to d) (mod n)



What happens in github ?
We generate public key for each machine.
We register this public key on github website.
Now github knows from which all public key it should accept the data. This is additional security.
Now public key will encrypt the message and pass to github along with public key. // Not sure whether it passes along with the public key
First of all github checks whether this public key is registered or not.
Then it takes the message, which can be decrypted by private key only.

Even if message gets hacked and reached to some other server it won't be able to decrypt it.


What does it mean to ssh into some server ?
//TODO
