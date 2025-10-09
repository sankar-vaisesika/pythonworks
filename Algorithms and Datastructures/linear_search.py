def linear_search(lst,target):

    for i in range(len(lst)):

        if lst[i]==target:

            print("found was found at index:",i)

            return

        
    print("target was not found on the list")


linear_search([1,2,4,21,12,4,6],12)

