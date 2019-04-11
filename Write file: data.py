data = [1, 3, 5, 7, 9]
with open("data.csv", 'w') as f:
    for i in data:
        f.write(str(i) + '\n')



