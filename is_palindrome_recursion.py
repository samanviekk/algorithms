def is_palindrome(s):
    return is_palindrome_helper(s, 0, len(s) - 1)


def is_palindrome_helper(s, i , j):
    if i == j or i > j:
        return True
    if not s[i].isalnum():
        return is_palindrome_helper(s, i + 1, j)
    if not s[j].isalnum():
        return is_palindrome_helper(s, i, j - 1)
    if s[i].casefold() != s[j].casefold():
        return False
    return is_palindrome_helper(s, i + 1, j - 1)

s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s3 = ""
s4 = "aa"
print(is_palindrome(s))
print(is_palindrome(s1))
print(is_palindrome(s3))
print(is_palindrome(s4))




