#palidrome
def ispalidrome(str1):
    x=str1[::-1]
    if x==str1:
        return True
    else:
        return False
str1=input("Enter the string to check: ")
print(ispalidrome(str1))