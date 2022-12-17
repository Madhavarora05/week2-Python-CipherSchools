#print list of odd and even differently from a list
list1=[1,2,3,4,5,6,7,8,9]
le=[]
lo=[]
for i in list1:
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)
print(lo,le)