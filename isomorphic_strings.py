def isomorphic(s, t):
    mydict = {}
    for i in range(len(s)):
        if s[i] in mydict:
            if mydict[s[i]] != t[i]:
                return False
            elif t[i] in mydict.values():
                return False
            else:
                mydict[s[i]] = t[i]
    return True

def is_isomorphic(s, t):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]] != t[i]:
                return False
        elif t[i] in d.values():
            return False
        else:
            d[s[i]] = t[i]
    return True


print(is_isomorphic('egg', 'add'))
print(is_isomorphic("foo", 'bar'))
print(is_isomorphic('title', 'paper'))