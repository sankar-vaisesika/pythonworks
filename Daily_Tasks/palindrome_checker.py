# Palindrome Sentence Checker (ignoring punctuation & case)

import re

def is_palindrome_sentence(s):

    # cleaned=re.sub(r"[^A-Za-z0-9]","",s).lower()

    # return cleaned==cleaned[::-1]

    #another method

    lst=[]

    for i in s:

        if i.isalnum():
            lst.append(i.lower())
        
    a="".join(lst)

    return a==a[::-1]    

s="A man, a plan, a canal: Panama"
print("palindrome sentence:",is_palindrome_sentence(s)) 