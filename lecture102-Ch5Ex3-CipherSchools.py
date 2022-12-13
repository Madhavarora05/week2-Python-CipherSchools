#reverse every string in list
list1=['abc','mno','xyz']
def rev(list1):
    list2=[]
    for i in list1:
        list2.append(i[::-1])
    return list2
print(rev(list1))