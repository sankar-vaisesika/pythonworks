def only_duplicates(st):
    
    count={}
    for c in st:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
            
    res=[]
    for c in st:
        if count[c]>1:
            res.append(c)
    
    return "".join(res)

print(only_duplicates("abcdef"))
print(only_duplicates("aabbcc"))
print(only_duplicates("banana"))



