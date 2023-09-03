inp_ = input("").split(" ")
arr = [int(inp_[0]), int(inp_[1]), int(inp_[2])]
arr.sort(reverse=True)
print(arr[-1], arr[0])