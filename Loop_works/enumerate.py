# Why enumerate() is used in python

# enumerate() is used in python when you want both index and value while looping over an iterable

#without enumerate()

items=["apple","orange",'banana']
i=0
for item in items:
    
    print(i,item)
    i+=1

#with enumerate()

for i,value in enumerate(items):

    print(i,value)

#looping through strings with position

for i,ch in enumerate("hello"):

    print(i,ch)

    