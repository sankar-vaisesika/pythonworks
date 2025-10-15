def duplicate_count(text):
    count = {}                    # Dictionary to store character counts
    text = text.lower()           # Convert the input to lowercase for case-insensitive comparison

    for char in text:
        if char in count:
            count[char] += 1      # Increment count if already exists
        else:
            count[char] = 1       # Initialize with 1

    duplicates = 0
    for v in count.values():      # Check how many values are > 1
        if v > 1:
            duplicates += 1

    return duplicates


print(duplicate_count(""))                  # 0 (empty string)
print(duplicate_count("abcde"))             # 0 (all unique)
print(duplicate_count("aabBcde"))           # 2 ('a' and 'b' each appear twice)
print(duplicate_count("Indivisibilities"))  # 2 ('i' and 's' appear more than once)


