ordering = []
while True:
    food = input("Food")
    if food == 'q':
        break
    price = input("Price")
    ordering.append([food, price])

print(ordering)

for i in ordering:
    print("The price of " + i[0] + " is " + i[1])