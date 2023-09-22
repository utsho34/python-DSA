arr = []
for i in range(16):
    arr.append(i)

def get_even_odd_list(array):
    even_array = []
    odd_array = []
    for i in range(len(array)):
        if i % 2 == 0:
            even_array.append(array[i])
        else:
            odd_array.append(i)
    print(f"Even List {even_array}")
    print(f"odd List {odd_array}")

get_even_odd_list(arr)