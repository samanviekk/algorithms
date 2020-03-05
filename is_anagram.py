def is_anagram(s, t):
    mydict = {}

    for i in s:
        if i in mydict:
            mydict[i] = mydict[i] + 1
        else:
            mydict[i] = 1
    for j in t:
        if j in mydict and mydict[j] > 0:
            mydict[j] = mydict[j] - 1
        else:
            return False
    return True

print(is_anagram('car', 'rac'))
print(is_anagram('cca', 'cat'))
