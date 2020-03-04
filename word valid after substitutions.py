def isValid(S: str) -> bool:
    mylist = []
    lookup = {'a': 'b', 'b': 'c'}
    for ch in S:
        if not mylist:
            if ch != 'a':
                return False
            else:
                mylist.append(ch)
        else:
            k = mylist[-1]
            if lookup[k] == ch:
                mylist.pop()
            if ch != 'c':
                mylist.append(ch)
    return not mylist



print(isValid('aabcabcbc'))