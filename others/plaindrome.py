tc = int(input())
t=1
while(tc>=1):
    num = int(input())
    temp = num
    rev = 0

    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        print(f"Case {t}: Yes")
    else:
        print(f"Case {t}: No")
    t=t+1
