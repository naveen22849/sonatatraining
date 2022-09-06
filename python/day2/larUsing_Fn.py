def largestnumber(n1,n2,n3):
    if type(n1) == str or type(n2) == str or type(n3) == str:
        return "please enter only numbers"
    elif n1>=n2 and n1>=n3:
        return "number 1 is large"
    elif n2>=n3:
        return "number 2 is large"
    else:
        return "number 3 is large"
print(largestnumber(8,65,65))