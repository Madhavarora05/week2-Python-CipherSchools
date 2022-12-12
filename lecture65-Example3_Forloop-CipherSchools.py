# ask user name and count each charcter
name=input("Enter Your name: ")
x=''
for i in range(len(name)):
    if name[i] not in x:
        print(name[i],":",name.count(name[i]))
        x+=name[i]
    else:
        continue