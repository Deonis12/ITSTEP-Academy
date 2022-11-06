mlist = [1, 'Anna', 0.254, 'John', ['Hello', 'John', 'nice to meet you'], 2.5]
for i in mlist:
    if isinstance(i, int):
        print('It is an integer',type(i))
    elif isinstance(i, str):
        print('It is an string',type(i))
    elif isinstance(i, float):
        print('It is floating number',type(i))
    elif isinstance(i,type(i)):
        print('It is list',type(i))