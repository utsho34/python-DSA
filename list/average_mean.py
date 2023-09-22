# array = [60,30,40]
# count = 0
# for i in array:
#     count+=i
# avg = float()
# print(f"Average mean of array is {count/len(array)}")

#with function
def find_average_mean(array):
    count = 0
    for i in array:
        count+=array[i]
    return count/len(array)

arr = [60,30,40]
avg=find_average_mean(arr)
print("{:.2f}".format(avg))


