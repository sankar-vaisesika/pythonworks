def longestCommonPrefix(strs):
    # If the list is empty, return empty string
    if not strs:
        return ""

    # Loop through characters of the first string
    for i in range(len(strs[0])):
        char = strs[0][i]

        # Compare with the same position in all other strings
        for s in strs[1:]:
            # If index out of range or characters don’t match, return the prefix so far
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    # If loop completes, the whole first string is a common prefix
    return strs[0]

# Example usage:
print(longestCommonPrefix(["flower", "flow", "flight"])) 
print(longestCommonPrefix(["racecar", "racer"])) 
