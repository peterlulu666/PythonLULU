#用户最多输入三次密码
#正确显示登录成功
#不正确显示错误，还有几次机会
psd = "correct"

count_psd = 0
chances = 3
while count_psd < 3:
    user_psd = input("type password: ")
    if user_psd == psd:
        print("log in")
        break
    else:
        print("type password again")
    count_psd += 1
    print(("you have " + str(chances - count_psd) + " chances"))









