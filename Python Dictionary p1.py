a = dict()      
b = open("C:\C PROGRAMS\VS CODE\words.txt")
for i in b:
    words = i.split()
    for i in words:
        if i in a: 
            continue
        a[i] = 1

c = input('Please enter the word you are looking for: \n')
if c in a:
    print('Found')
else:
    print('Not found')
