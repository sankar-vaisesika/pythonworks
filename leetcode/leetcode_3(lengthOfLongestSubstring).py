def lengthOfLongestSubstring(s):

    l=0

    res=0

    charSet=set()

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1

        charSet.add(s[r])
        res=max(res,r-l+1)

    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

#working
# | Step | `left`  | `right` | `seen`                    | Substring | `max_len` |
# | ---- | ------- | ------- | ------------------------- | --------- | --------- |
# | 1    | 0       | 0       | {a}                       | "a"       | 1         |
# | 2    | 0       | 1       | {a,b}                     | "ab"      | 2         |
# | 3    | 0       | 2       | {a,b,c}                   | "abc"     | 3         |
# | 4    | 0→1→2→3 | 3       | {a,b,c} → a seen → shrink | "bca"     | 3         |
