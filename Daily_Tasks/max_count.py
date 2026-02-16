
from collections import Counter

lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]

# count=Counter(lst)

# max_count=max(count.values())

# max_keys=[k for k,v in count.items() if v==max_count]

# print(max_keys)
#or

count={}

for num in lst:
    if num in count:
        count[num]+=1
    else:
        count[num]=1

max_count=max(count.values())
max_keys=[k for k,v in count.items() if v==max_count]
print(max_keys)