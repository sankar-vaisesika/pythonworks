def quicksort(values):

    if len(values)<=1:

        return values
    
    less_than_pivot=[]

    greateer_than_pivot=[]

    pivot=values[0]

    for value in values[1:]:

        if value<=pivot:

            less_than_pivot.append(value)

        else:

            greateer_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] +quicksort(greateer_than_pivot)


print(quicksort([3,2,1,5,6,3,2]))