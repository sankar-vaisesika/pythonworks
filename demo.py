import copy

original=[[1,2],[3,4]]

shallow=copy.copy(original)

shallow[0][0]=99

print(original)


original=[[1,2],[3,4]]

deep=copy.deepcopy(original)

deep[0][0]=99

print(original)

#________________________________________

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:

    if "a" in x:

        newlist.append(x)

print(newlist)

newlist=[x for x in fruits if "a" in x]

print(newlist)

#______________

org=[1,2,3]

shallow_1=copy.deepcopy(org)

shallow_1[1]=100

print(org)