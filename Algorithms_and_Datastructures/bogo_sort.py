import random

def is_sorted(values):

    for i in range(len(values)-1):

        if values[i]>values[i+1]:

            return False
        
    return True

values=[5,3,2,9,6,8]

print(is_sorted(values))

def bog_sort(values):
    attempts=0
    while not is_sorted(values):
        # attempts+=1
        # print(attempts)
        random.shuffle(values)

    return values

print(bog_sort(values))