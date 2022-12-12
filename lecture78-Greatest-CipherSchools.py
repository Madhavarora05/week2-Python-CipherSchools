def greatest(a,b,c):
    if a>b and a>c:
        return f"{a} is greatest"
    elif b>a and b>c:
        return f"{b} is greatest"
    else:
        return f"{c} is greatest"
num1=int(input("1st number: "))
num2=int(input("2nd number: "))
num3=int(input("3rd number: "))
print(greatest(num1,num2,num3))