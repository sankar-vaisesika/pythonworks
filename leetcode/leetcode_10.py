import re
pattern=input("Enter pattern:")
text=input("ENter text:")

match=re.search(pattern,text)

if match:
    print("match found")
    print("Matched text:",match.group())

else:
    print("No match found")