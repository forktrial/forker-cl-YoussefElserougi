# student_code.py

def palindrome_permutation(s: str) -> bool:
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Dictionary to count character frequencies
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check the number of characters that have an odd count
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    # For a string to be a permutation of a palindrome:
    # At most one character can have an odd count
    return odd_count <= 1

