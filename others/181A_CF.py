n, m = map(int, input().split())
l = x = 0
for i in range(n):
    a = list(input())
    for j in range(m):
        if a[j] == '*':
            l ^= (i + 1)
            x ^= (j + 1)

print(l, x)