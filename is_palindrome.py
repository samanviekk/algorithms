def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i = i + 1
            continue
        if not s[j].isalnum():
            j = j - 1
            continue
        if s[i].casefold() != s[j].casefold():
            return False
        else:
            i += 1
            j -= 1
    return True

s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = ""
print(is_palindrome(s))
print(is_palindrome(s1))
print(is_palindrome(s2))



