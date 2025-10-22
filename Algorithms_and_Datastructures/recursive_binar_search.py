
def recursive_binary_search(lst,target):

    if len(lst)==0:

        return False
    
    else:

        midpoint=len(lst)//2

    
    if lst[midpoint]==target:

        return midpoint
    
    elif lst[midpoint]<target:

        return recursive_binary_search(lst[midpoint+1:],target)
    
    else:

        return recursive_binary_search(lst[:midpoint],target)



print(recursive_binary_search([1, 2, 4, 6, 12, 21, 21],4))
