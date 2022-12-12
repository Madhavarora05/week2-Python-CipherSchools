#Function Practice
def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"
num=int(input("Enter Number: "))
print(odd_even(num))