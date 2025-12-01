# Check if a string is a pangram (contains every letter of the alphabet at least once)
def is_pangram(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"

    s=s.lower()
    found_letter=set()
    for ch in s:
        if ch in alphabet:
            found_letter.add(ch)
    
    return len(found_letter)==len(alphabet)
print(is_pangram("The quick brown fox jumps over the lazy dog"))