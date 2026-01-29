def is_happy(n):
    seen=set()
    # Continue until n becomes 1 (Happy) or we hit a number we've seen (Cycle)

    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        n=sum(int(digit)**2 for digit in str(n))

    return n==1
print(is_happy(19))
print(is_happy(2))
