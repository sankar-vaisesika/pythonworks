def merge_sorted_arrays(m,n):
    res=[]
    i=j=0
    while i<len(m) and j<len(n):
        if m[i]<=n[j]:
            res.append(m[i])
            i+=1

        else:
            res.append(n[j])
            j+=1
    res.extend(m[i:])
    res.extend(n[j:])

    return res
print(merge_sorted_arrays([1,2,3],[2,5,6]))
print(merge_sorted_arrays([1],[]))
print(merge_sorted_arrays([0],[1]))
