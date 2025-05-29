
# from collections import Counter

# lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]

# count=Counter(lst)

# max_count=max(count.values())

# max_keys=[k for k,v in count.items() if v==max_count]

# print(max_keys)


lst=[1,2,2,3,1,4,1,2,4,3,1,5,2]
from collections import Counter

count=Counter(lst)

print(count)

max_count=max(count.values())

print(max_count)

max_keys=[k for k,v in count.items() if v==max_count]

print(max_keys)