from collections import Counter
def duplicate_count(text):

    count={}

    text=text.lower()

    for char in text:

        if char in count:

            count[char]+=1

        else:

            count[char]=1

    duplicates=0

    for v in count.values():

        if v>1:

            duplicates+=1

    return duplicates

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("Indivisibilities"))
x=9/2
print(x)