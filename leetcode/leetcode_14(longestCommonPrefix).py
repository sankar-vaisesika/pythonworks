
def longestCommonPrefix(strs):

    res=""

    for i in range(len(strs[0])): #loop over characters of first string

        for s in strs:            #loop through all strings in the list
            
            if i==len(s) or s[i]!=strs[0][i]:    # If index exceeds current string or char doesn't match with first string

                return res

        res+=strs[0][i]   # If all strings have the same char at index i, add to result
    
    return res


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car "]))


    