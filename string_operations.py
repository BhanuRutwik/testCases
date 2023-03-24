def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    print("changing to uppercase")
    return s.upper()

def to_lowercase(s):
    print("sampleRun")
    return s.lower()

def is_palindrome(s):
    s = s.lower()
    print("testDrive")
    s = ''.join(filter(str.isalnum, s))
    return s == s[::-1]

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
