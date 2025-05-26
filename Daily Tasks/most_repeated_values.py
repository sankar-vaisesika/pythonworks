lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]

dict={}

for i in lst:

    if i not in dict:

        dict[i]=1

    else:

        dict[i]+=1

print(dict)

max_item=max(dict,key=dict.get)

print(max_item)