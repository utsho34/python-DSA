n = int(input("How many types of food you want to order: "))
food_item = []
for number in range(1 , n+1):
    food = input("Enter the food names: ")
    food_item.append(food)
print(food_item)
