#using sliding algorithm

def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # If the character is already in the map and within the current window
        if char in char_map and char_map[char] >= left:
            # Move the left pointer to the next position after the last occurrence
            left = char_map[char] + 1
        
        # Update the character's last seen index
        char_map[char] = right
        
        # Calculate the current window size and update max_length
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Example Usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # Output: 1 ("b")
print(length_of_longest_substring("pwwkew"))    # Output: 3 ("wke")


