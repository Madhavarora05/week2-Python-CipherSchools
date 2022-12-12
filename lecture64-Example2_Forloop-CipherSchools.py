#calculate sum of digits of user inputed number
num=input("Enter Number: ")
sum=0
for i in range(len(num)):
    sum=sum+int(num[i])
print(f"Sum of digits of {num} is {sum}")