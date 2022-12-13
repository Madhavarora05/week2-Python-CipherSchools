#Returning list with sqaure of items of first list
def sqlist(list1):
    list2=[]
    for i in list1:
        list2.append(i**2)
    return list2
list1=[1,2,3,4,5,6]
print(sqlist(list1))