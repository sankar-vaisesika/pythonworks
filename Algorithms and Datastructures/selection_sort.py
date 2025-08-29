# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# for i in range(len(my_array)-1):

#     min_index=i

#     for j in range(i+1,len(my_array)):

#         if my_array[j]<my_array[min_index]:

#             min_index=j

#     min_value=my_array.pop(min_index)

#     my_array.insert(i,min_value)

# print("Sorted array is:",my_array)


#-----------------Another Method-------------------#

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# for i in range(len(my_array)-1):

#     min_index=i

#     for j in range(i+1,len(my_array)):

#         if my_array[j]<my_array[min_index]:

#             min_index=j

#     my_array[i],my_array[min_index]=my_array[min_index],my_array[i]

# print("Sorted array:",my_array)


#-----------------Another Method-------------------#


def selection_sort(values):

    sorted_list=[]

    for i in range(0,len(values)):

        index_to_move=index_of_min(values)

        sorted_list.append(values.pop(index_to_move))

    return sorted_list

def index_of_min(values):
    
    min_index=0

    for i in range(1,len(values)):

        if values[i]<values[min_index]:

            min_index=i

    return min_index

print(selection_sort([64, 34, 25, 12, 22, 11, 90, 5]))