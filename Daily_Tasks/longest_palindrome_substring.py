


def longest_substring(s):

    if len(s)==0:
        return ""
    
    best=s[0]

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub=s[i:j]

            if sub==sub[::-1] and len(sub)>len(best):

                best=sub

    return best
print(longest_substring("babad"))
print(longest_substring("cbbd"))
print(longest_substring("c"))
    