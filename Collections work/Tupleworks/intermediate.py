# Unpack a tuple into variables

tp=("Ram","Sam","Tom")

(x,y,z)=tp

print(x,y,z)

# Swap two variables using tuple unpacking

x,y=y,z

print(x,y,z)

# Loop through a tuple using for loop

for i in tp:

    print(i)

# Sort elements of a tuple (convert to list, sort, convert back)

tp=(4,2,1,5,7,8,3)

tp=list(tp)

tp.sort()

tp=tuple(tp)

print(tp)


# Find max, min, and sum of a numeric tuple

tup=(5,2,1,6,7,4)

print("Max is ",max(tup))

print("Min is ",min(tup))

print("Sum is",sum(tup))
# Merge multiple tuples into one

tup3=tp+tup

print(tup3)

# Slice a tuple (e.g., first 3 elements, last 2, etc.)

tup=(2,1,4,2,5,7,5)

print(tup[0:3])

print(tup[-3:-1])

# Nest one tuple inside another

tp1=(1,2,3,4)

tp2=("car","bike",tp1)

print(tp2)

# Use tuple as a key in a dictionary

tp1=(1,2,3,4)

dict={}

dict[tp1]="value"

print(dict)

# Check if all items in a tuple are the same

tup=(2,1,4,2,5,7,5)


if len(set(tup))==1:

    print("All are same")

else:

    print("Not same")