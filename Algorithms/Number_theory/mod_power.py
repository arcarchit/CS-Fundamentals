a = 2
k = 3
n = 7
# I think we are assuming a < n here.
def mod_power(a, k, n):
    if k == 0:
        return 1
    if k == 1:
        return a
    q, r = divmod(k, 2)
    if r==0:
        return mod_power((a*a) % n, q, n)
    else:
        return mod_power((a*a) % n, q, n) * a % n
        # We need to understand property of modular multiplication
        # and it would be (a * b) % n = ((a %n) * (b %n)) % n


print mod_power(2, 13739062, 13739063)
print mod_power(a, k ,n)
