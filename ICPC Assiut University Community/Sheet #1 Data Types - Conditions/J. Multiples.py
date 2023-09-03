inp_ = input("").split(" ")
x = int(inp_[0]) / int(inp_[1])
x2 = int(inp_[1]) / int(inp_[0])
if x == int(x) or  x2 == int(x2):
    print("Multiples")
else:
    print("No Multiples")