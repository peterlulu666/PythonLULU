ordering = []
while True:
    food = input("Food")
    if food == 'q':
        break
    price = input("Price")
    order = []
    order.append(food)
    order.append(price)
    ordering.append(order)

print(ordering)

for i in ordering:
    print("The price of the " + i[0] + " is " + i[1] + " dollars.")