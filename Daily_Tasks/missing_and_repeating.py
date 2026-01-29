def find_missing_and_repeating(arr):
    seen=set()
    repeating=-1
    missing=-1
    for num in arr:
        if num in seen:
            repeating=num
        seen.add(num)
    for i in range(1,len(arr)+1):
        if i not in seen:
            missing=i
            break
    return missing,repeating
print(find_missing_and_repeating([4,3,6,2,1,1]))