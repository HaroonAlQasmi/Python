user_input= int(input("Enter an Integer:"))
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