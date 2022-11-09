print('Task 1:')

tuple1 = (1,2,3,4,5,6)
tuple2 = (3,5,2,9)
tuple3 = (2,8,5,4,7,9)
tuple1_3 = []
for i in tuple1:
    if i in tuple2 and i in tuple3:
        tuple1_3.append(i)
print(tuple1_3)

print('\nTask2')

data1 = [1,2,1,4,2,7]
data2 = [2,5,7,5,8]
data3 = [6,3,6,7,4,7]

a = [i for i in data1 if data1.count(i)==1]
b = [i for i in data2 if data2.count(i)==1]
c = [i for i in data3 if data3.count(i)==1]

print('',a,'\n',b,'\n',c)

print('\nTask3:')

tupletest = [(1,2,3,4,5,6),(3,5,2,9),(2,8,5,4,7,9)]

c = [i for i in tupletest if i[3]==4]
print(c)