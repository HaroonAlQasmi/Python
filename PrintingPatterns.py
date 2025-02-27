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

"""
1           (10^0 + 0) * (10^0 + 0)     
121         (10^1 + 1) * (10^1 + 1)
12321       (10^2 + 11) * (10^1 + 11)
1234321     (10^3 + 111) * (10^3 + 111)
123454321   (10^4 + 1111) * (10^4 + 1111)
"""
import math

no_of_rows = 5
prev_res = 0
count = 0

# curr_res = math.pow(10, count) + prev_res  # 1 + 0 (count = 0)
# count += 1
# prev_res = curr_res
# print(curr_res)  # 1

# curr_res = math.pow(10, count) + prev_res # 10 + 1 = 11  (count = 1)
# count += 1
# prev_res = curr_res
# print(curr_res)  # 11

# curr_res = math.pow(10, count) + prev_res # 100 + 11 = 111  (count = 2)
# count += 1
# prev_res = curr_res
# print(int(curr_res))  # 11

for line_no in range(no_of_rows):
    prev_res = math.pow(10, line_no) + prev_res 
    print(int(prev_res) * int(prev_res))
