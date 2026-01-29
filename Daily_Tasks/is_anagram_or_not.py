def is_anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    return sorted(str2)==sorted(str1)
print(is_anagram("Listen","Silent"))