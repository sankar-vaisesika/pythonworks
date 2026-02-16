# Return the k most frequent elements in a list.

def top_k_frequent(nums, k):
    freq = {}    
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
    result=[]
    for i in range(k):
        result.append(sorted_items[i][0])

    return sorted_items


print(top_k_frequent([1,1,1,2,2,3],2))
print(top_k_frequent([4,1,-1,2,-1,2,3],2))