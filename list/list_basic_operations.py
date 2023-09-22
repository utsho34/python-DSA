list = []
for i in range(1000):
    list.append(i)
print(len(list))
list.pop()
print(list[-1])
list.append(10)
print(list[-1])
if 10 in list:
    print(list.index(50))