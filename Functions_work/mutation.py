def mutate_string(s,position,char):
    # return s[:position]+char+s[position+1:]
    l=list(s)
    l[position]=char
    s="".join(l)
    return s
s="abracadabra"
position=5
char="k"
print(mutate_string(s,position,char))

