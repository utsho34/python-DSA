import sys

def max_permutation(n, k):
    sol = []
    switch = k
    if k == 0:
        return [x for x in range(1, n+1)]
    
    if n % (2*k) != 0:
        return [-1]
        
    for p in range(1, n + 1):
        sol.append(p + switch)
        
        if p % k == 0:
            switch *= -1
            
    return sol
        
        

t = int(input().strip())
for i in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n),int(k)]
    
    print(" ".join(list(map(str, max_permutation(n, k)))))