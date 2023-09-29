n = int(input())
list = [n]
for i in range(0,n):
    j = int(input())
    list.append(j)
list.sort()
count = 0;
for i in range(0,n):
    count = count+ (list[n]-list[i+1])
print(count)
