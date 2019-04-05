#用户最多输入三次密码
#正确显示登录成功
#不正确显示错误，还有几次机会

psd = "correct"
count_chances = 3
while count_chances >0:
    count_chances -= 1
    user_psd = input("type password: ")
    if user_psd == psd:
        print("log in")
        break
    else:
        print("password is incorrect ")
        if count_chances > 1:
            print("You have " + str(count_chances) + " chances")
        elif count_chances == 1:
            print("You have " + str(count_chances) + " chance")
        else:
            print("the account has been locked")













