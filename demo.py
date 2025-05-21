import copy

original=[[1,2],[3,4]]

shallow=copy.copy(original)

shallow[0][0]=99

print(original)

#or

lst1=[[1,2],[3,4]]

lst2=lst1.copy()

lst2[0][0]=99

print(lst1)


#_______________________________________


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

#______________________________




lst=[1,1]

n=8

while len(lst)<n:

    c=lst[-1]+lst[-2]

    lst.append(c)

    

print(lst)
#_________________________________

lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]

dict={}

for item in lst:
    if item in dict:
        dict[item]+=1

    else:

        dict[item]=1    

print(dict)

max_item=max(dict,key=dict.get)

print(max_item)