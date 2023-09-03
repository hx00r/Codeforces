inp_ = input("")
if ord(inp_) <= 57:
    print("IS DIGIT")
elif ord(inp_) <= 90:
    print("ALPHA\nIS CAPITAL") 
elif ord(inp_) <= 122:
    print("ALPHA\nIS SMALL")