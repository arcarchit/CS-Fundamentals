a = 123456789
b = 987654321

def gcd(a, b):
    r = a % b
    if r==0:
        return b
    else:
        return gcd(b, r)


print gcd(a,b)
