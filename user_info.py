psd = "correct"

count_psd = 0
while count_psd < 3:
    user_psd = input("type password: ")
    if user_psd == psd:
        print("log in")
        break
    else:
        print("type password again")
    count_psd += 1
    print(("you have " + str(3 - count_psd) + " chances"))









