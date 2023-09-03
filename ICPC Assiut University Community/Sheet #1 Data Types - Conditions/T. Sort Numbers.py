n = input("").split(" ")
n_int = sorted(map(int, n)) # convert list from str to int
ns = sorted(n_int)
print(f"{ns[0]}\n{ns[1]}\n{ns[2]}\n")
print(f"{n[0]}\n{n[1]}\n{n[2]}")