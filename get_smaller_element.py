# get smaller element of a list compare with an element provide by user
arr = []
i=10
for k in range (12):
    arr.append(i)
    i+=3
comp_val = int(input("Enter a number for comparison: "))
smaller_list = []
for j in range(len(arr)):
    if arr[j] < comp_val:
        smaller_list.append(arr[j])
print(smaller_list)
# we can direct run loop to the array, but i'm using the index for my personal interest.