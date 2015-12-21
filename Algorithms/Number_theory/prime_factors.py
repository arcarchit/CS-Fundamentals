input = 400

def factor1(input):
    ans = []
    d = 2
    while (input != 1):
        if input % d ==0:
            ans.append(d)
            input = input/d
        else:
            d = d + 1
    return ans


def factor2(input):
    ans = []
    d = 2
    while (input >= d * d): # change is made here (d * d)
        if input % d ==0:
            ans.append(d)
            input = input/d
        else:
            d = d + 1
    if input > 1:   # Changes here as well, what if input is 25, we want to include 5 two times
        ans.append(input)
    return ans

print factor1(input)
print factor2(input)
