def check_palindrome(strng) -> bool:
    normalized_string = ''.join(strng.lower().split())
    return normalized_string == ''.join(reversed(normalized_string))

string1 = 'Ol llal llo'

print(check_palindrome(string1))
