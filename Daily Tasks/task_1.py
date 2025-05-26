# lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]

# dict={}

# for i in lst:

#     if i not in dict:

#         dict[i]=1

#     else:

#         dict[i]+=1


# max_item=max(dict.values())

# max_keys=[k for k,v in dict.items() if v==max_item]

# print(max_item)

#optimized code

lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]

from collections import Counter

count=Counter(lst)

max_count=max(count.values())

max_keys=[k for k,v in count.items() if v==max_count]

print(max_keys)