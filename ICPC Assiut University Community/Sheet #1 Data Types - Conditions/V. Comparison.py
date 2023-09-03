eq = input("").split(" ")
if '<' in eq:
    if int(eq[0]) < int(eq[-1]):
        print("Right")
    else:
        print("Wrong")
elif '>' in eq:
    if int(eq[0]) > int(eq[-1]):
        print("Right")
    else:
        print("Wrong")
else:
    if int(eq[0]) == int(eq[-1]):
        print("Right")
    else:
        print("Wrong")