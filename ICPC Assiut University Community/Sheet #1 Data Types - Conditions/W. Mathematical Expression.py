eq = input("").split(" ")
if '+' in eq:
    if int(eq[0]) + int(eq[-3]) == int(eq[-1]):
        print("Yes")
    else:
        print(int(eq[0]) + int(eq[-3]))
elif '-' in eq:
    if int(eq[0]) - int(eq[-3]) == int(eq[-1]):
        print("Yes")
    else:
        print(int(eq[0]) - int(eq[-3]))
else:
    if int(eq[0]) * int(eq[-3]) == int(eq[-1]):
        print("Yes")
    else:
        print(int(eq[0]) * int(eq[-3]))