txt = "The rain in Spain"

import re
#findall
x=re.findall(r"ai",txt)

print(x)

#search-- first occurence of the match in the string

x=re.search(r"a",txt)

print(x.start())

#split

x=re.split(r"\s",txt)
print(x)

x=re.split(r"\s",txt,2)
print(x)

#sub

x=re.sub(r"\s","___",txt)

print(x)