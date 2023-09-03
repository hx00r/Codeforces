n = float(input(""))
n, dec = divmod(n, 1)
if dec == 0:
    print("int", int(n))
else:
    print("float", int(n), round(dec, 3))