value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
"""
Now I want to solve this by dynamic programming
Every dynamic programming problem has three steps:
1. Simple subproblems
2. Subproblem optimization
3. Subproblem overlap
"""
ans= [None]*(capacity+1)

for w in range(0, capacity+1):
    ans[w]=0

for k in range(0, len(weight)):
    current_weight = weight[k]
    current_value = value[k]
    # We need value form previous row only, so we are using just 1D array overriding previous row
    for w in range(capacity, current_weight-1, -1):
        if(ans[w-current_weight]+current_value > ans[w]):
            ans[w] = ans[w-current_weight] + current_value

print ans
