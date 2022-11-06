mystr = input("Enter your text: ").split()
list1=input("Enter your reserved list: ").split()
list2=[]
for i in mystr:
    if i not in list1:
        list2 += [i]
    else:
        list2 += [i.upper()]
mystr1 = " ".join(list2)
print(mystr1)
