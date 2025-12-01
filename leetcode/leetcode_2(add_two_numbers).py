# Add Two Numbers

def add_two_numbers(l1,l2):
    c=0
    i,j=0,0
    res=[]
    while i<len(l1) or j<len(l2) or c:
        d1=l1[i] if i<len(l1) else 0
        d2=l2[j] if j<len(l2) else 0
        current_sum=d1+d2+c
        res_sum=current_sum%10
        c=current_sum//10
        i+=1
        j+=1

        res.append(res_sum)
    return res

print(add_two_numbers([2,4,3],[5,6,4]))
print(add_two_numbers([0],[0]))
print(add_two_numbers([9,9,9,9,9,9,9],[9,9,9,9]))
