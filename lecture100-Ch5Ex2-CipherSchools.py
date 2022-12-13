#reverse the list infunction using pop and append
def rev(l):
    list1=[]
    for i in range(len(l)):
        x=l.pop()
        list1.append(x)
    return list1
list1=[5,6,4,3]
print(rev(list1))