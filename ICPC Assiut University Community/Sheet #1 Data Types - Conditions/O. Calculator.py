inp_ = input("")
if '+' in inp_:
    nums = inp_.split('+')   
    print(int(nums[0]) + int(nums[1]))
elif '-' in inp_:
    nums = inp_.split('-')   
    print(int(nums[0]) - int(nums[1]))
elif '*' in inp_:
    nums = inp_.split('*')   
    print(int(nums[0]) * int(nums[1]))
else:
    nums = inp_.split('/')   
    print(int(int(nums[0]) / int(nums[1])))


# inp_ = input("")
# op = {'+': lambda x, y: x + y,
#       '-': lambda x, y: x - y,
#       '*': lambda x, y: x * y,
#       '/': lambda x, y: x / y,
# }
# for i in op:
#     if i in inp_:
#         nums = inp_.split(i)
#         print(op[i](int(nums[0]), int(nums[1])))
#         break