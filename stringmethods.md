1. center()-Centers the string with padding.
```
"hello".center(10, "-")   # '--hello---'
```
2. count()-Counts occurrences of a substring.x
```
"banana".count("a")   # 3
```
3. encode()-Encodes the string using UTF-8 by default.
```
"hello".encode()   # b'hello'
```
4. endswith()-Checks if string ends with a given substring.
```
"hello!".endswith("!")   # True
```
5. expandtabs()-Sets tab size.
```
"hello\tworld".expandtabs(4)    #hello   world
```
6. find()-Returns index of first occurrence (or -1).
```
"hello world".find("world")   # 6
```
7. format()-String formatting.
```
"Hello {}".format("Jaya")   # 'Hello Jaya'
```
8. format_map()-Formatting using dictionary.
```
data = {"name": "Jaya"}
"Hello {name}".format_map(data)
```
9. index()-Like find() but raises error if not found.
```
"hello".index("e")   # 1
```
10. isalnum()-Checks if all chars are alphanumeric.
```
"abc123".isalnum()   # True
```
11. isalpha()-Checks if all chars are alphabetic.
```
"abc".isalpha()   # True
```
12. isascii()-Checks if all chars are ASCII.
```
"hello".isascii()   # True
```
13. isdecimal()-Checks decimal characters.
```
"123".isdecimal()   # True
```
14. isdigit()-Checks digits (includes superscripts).
```
"²".isdigit()   # True
```
15. isidentifier()-Checks valid Python identifier.
```
"my_var".isidentifier()   # True
```
16. islower()-Checks if all chars are lowercase.
```
"hello".islower()   # True
```
17. isnumeric()-Checks numeric characters (includes fractions, Roman numerals).
```
"Ⅷ".isnumeric()   # True
```
18. isprintable()-Checks printable characters.
```
"hello!".isprintable()   # True
```
19. isspace()-Checks whitespace characters.
```
"   ".isspace()   # True
```
20. istitle()-Checks "Title Case".
```
"Hello World".istitle()   # True
```
21. isupper()-Checks uppercase.
```
"HELLO".isupper()   # True
```
22. join()-Joins iterable elements into a string.
```
"-".join(["a", "b", "c"])   # 'a-b-c'
```
23. ljust()-Left-justifies the string.
```
"hi".ljust(5, ".")   # 'hi...'
```
24. lower()-Converts to lowercase.
```
"HELLO".lower()   # 'hello'
```
25. lstrip()-Trims left side whitespace (or characters).
```
"  hello".lstrip()   # 'hello'
```
26. maketrans()-Creates translation mapping.
```
table = str.maketrans({"a":"@", "e":"3"})
"apple".translate(table)   # '@ppl3'
```
27. partition()-Splits into 3 parts: before, separator, after.
```
"hello-world".partition("-")
# ('hello', '-', 'world')
```
28. replace()-Replaces substring.
```
"banana".replace("a", "o")   # 'bonono'
```
29. rfind()-Returns last occurrence index.
```
"banana".rfind("a")   # 5
```
30. rindex()-Like rfind() but raises error if not found.
```
"banana".rindex("a")   # 5
```
31. rjust()-Right-justifies string.
```
"hi".rjust(5, ".")   # '...hi'
```
32. rpartition()-Right-most partition.
```
"hello-world-test".rpartition("-")
# ('hello-world', '-', 'test')
```
33. rsplit()-Splits from the right.
```
"a,b,c".rsplit(",", 1)   # ['a,b', 'c']
```
34. rstrip()-Trims right side whitespace or characters.
```
"hello...".rstrip(".")   # 'hello'
```
35. split()-Splits string.
```
"a b c".split()   # ['a', 'b', 'c']
```
36. splitlines()-Splits on line breaks.
```
"hello\nworld".splitlines()
```
37. startswith()-Checks prefix.
```
"python".startswith("py")   # True
```
38. strip()-Trims both sides.
```
"  hello  ".strip()   # 'hello'
```
39. swapcase()-Swaps case.
```
"HeLLo".swapcase()   # 'hEllO'
```
40. title()-Converts to title case.
```
"hello world".title()   # 'Hello World'
```
41. translate()-Applies translation table.
```
table = str.maketrans("ae", "@3")
"peace".translate(table)   # 'p3@c3'
```
42. upper()-Converts to uppercase.
```
"hello".upper()   # 'HELLO'
```
43. zfill()-Pads left with zeros.
```
"42".zfill(5)   # '00042'
```