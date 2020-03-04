def is_wellformed(s):
    left_chars = []
    lookup = {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars:
            return False
        else:
            key = left_chars.pop()
            if lookup[key] != c:
                return False
    return True if len(left_chars) == 0 else False


mystr = '([](){})'
print(is_wellformed(mystr))
