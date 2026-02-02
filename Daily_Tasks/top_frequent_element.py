# Return the k most frequent elements in a list.

def top_k_frequent(nums, k):
    freq = {}

    
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    sorted_items=sorted(freq.items())
    result=[]
    for i in range(k):
        result.append(sorted_items[i][0])

    return result


print(top_k_frequent([1,1,1,2,2,3],2))