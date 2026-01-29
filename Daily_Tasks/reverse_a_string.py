def reverse(s):
    reversed_s=""
    for c in s:
        reversed_s=c+reversed_s
    return reversed_s
print(reverse("asasaa"))