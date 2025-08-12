

def binary_search(lst,target):

    first=0
    last=len(lst)-1


    while first<=last:
        mid=(first+last)//2
        
        if target==lst[mid]:

            print("target found at index",mid)

            return 
        
        elif lst[mid]<target:

            first=mid+1

        else:
            last=mid-1

    print("not found")
    

binary_search([1, 2, 4, 6, 12, 21, 21],4)
