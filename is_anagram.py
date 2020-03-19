def is_anagram(s, t):
    mydict = {}
    if len(s) != len(t):
        return False
    
    for i in s:
        mydict[i] = mydict.get(i, 0) + 1
    print(mydict.items())
    for j in t:
        if j in mydict and mydict[j] > 0:
            mydict[j] = mydict[j] - 1
        else:
            return False
    return True

print(is_anagram('car', 'rac'))
print(is_anagram('cca', 'cat'))
print(is_anagram('ab', 'a'))
