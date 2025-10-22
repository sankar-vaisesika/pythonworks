from re import finditer

text="abababbaab"
    # 0123456789
x=finditer(r"ab",text)

for m in x:

    print(m.start(),m.group())

text="fatcatrunsveryfasttocatchtherat"

y=finditer(r"(at)",text)

for obj in y:

    print(obj.start(),obj.group())

text="I have 3 cars,3 bike and 1 Cycle"

# x=finditer(r"[a-z]",text)
# x=finditer(r"[A-Z]",text)
# x=finditer(r"[0-9]",text)
# x=finditer(r"[a-zA-Z]",text)
x=finditer(r"[^a-zA-Z]",text)



for obj in x:

    print(obj.start(),"==>",obj.group())