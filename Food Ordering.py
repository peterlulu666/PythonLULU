ordering = []
while True:
    food = input("Food")
    if food == 'q':
        break
    price = input("Price")
    ordering.append([food, price])

print(ordering)

for i in ordering:
    print("The price of the " + i[0] + " is " + i[1] + " dollars.")

with open("food.csv", 'w') as f:
    for i in ordering:
        f.write(i[0] + ',' + i[1] + '\n')
