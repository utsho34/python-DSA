def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
        # sum=str(sum)
    print(sum)


ar_count = int(input())

ar = list(map(int, input().rstrip().split()))
aVeryBigSum(ar)

#TODO - have to solve it with c++. Hopefully need to use unsigned long long int
