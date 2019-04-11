#随机数1～100
#重复猜数字
#猜对显示猜对
#猜错显示比答案大还是小

import random

r = random.randint(1,100)
guess_count = 0

while True:
    guess_count += 1
    user_guess = int(input("Gusee a number"))
    if user_guess == r:
        print("The number guessed is correct")
        print("You guessed " + str(guess_count) + " times")
        break
    else:
        if user_guess < r:
            print("The number guessed is incorrect, " + "it is too low")
        else:
            print("The number guessed is incorrect, " + "it is too high")
    print("You guessed " + str(guess_count) + " times")








