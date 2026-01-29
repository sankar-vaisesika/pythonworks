def next_greater_element(arr):
    stack=[]
    result=[-1]*len(arr)
    for i in range(len(arr)): #0    1       2       3
        while stack and  arr[i]>arr[stack[-1]]:
            index=stack.pop()
            result[index]=arr[i]#   [5,-1,-1,-1]
        stack.append(i)     #[0]    [1]    [1,2]    [3] 
    return result
print(next_greater_element([4, 5, 2, 10]))
print(next_greater_element([2,4,0,9,6]))
print(next_greater_element([1,2,3,4,3]))
print(next_greater_element([1,2,1]))

#i             arr[i]                   stack                   Result
#0                4                     [0]                   [-1,-1,-1,-1]
#1                5                     [1]                   [5,-1,-1,-1]
#2                2                     [1,2]                  [5,-1,-1,-1]
#3                10                    [3]                    [5,10,10,-1]

