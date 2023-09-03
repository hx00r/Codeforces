import math

inp_ = input("").split(" ")
number = int(inp_[0]) / int(inp_[1])
_, decimal_part = divmod(number, 1)
print(f"floor {inp_[0]} / {inp_[1]} = {math.floor(number)}")
print(f"ceil {inp_[0]} / {inp_[1]} = {math.ceil(number)}")
print(f"round {inp_[0]} / {inp_[1]} = {round(number) if decimal_part < 0.5 else math.ceil(number)}")