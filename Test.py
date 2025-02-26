#this file is for testing ideas


user_input= input("Enter an Integer:")
valid_input = True
while valid_input:
    if type(user_input) == int:
        user_input = int(user_input)

        for num in range(1, user_input+1):
            for sum in range(1, num + 1):
                print(sum, end="")
            print("")
        for num in range(1, user_input+1):
            for sum in range(1, num + 1):
                print("*", end="")
            print("")
        for num in range(1,user_input + 1):
            spaces = " " * (user_input-num)
            stars = "*" * (2*num-1)
            print(spaces+stars)
            valid_input = False
    else:
        print("WRONG INPUT")