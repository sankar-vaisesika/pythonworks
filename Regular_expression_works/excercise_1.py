# from re import finditer
import re
text="abbbababbabaaaab"

# x=finditer(r"b{2,3}",text)

# for obj in x:

#     print([obj.start(),obj.group()])

y=re.search(r"world$","Hello world")

# for obj in y:

#     print(obj.start(),obj.group(),end=" ")


print(bool(y))