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
