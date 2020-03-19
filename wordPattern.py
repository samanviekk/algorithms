def word_pattern(pattern, str):

    patternHash = {}
    wordHash = {}
    words = str.split()
    if len(pattern) != len(words):
        return False

    #for p, w in zip(pattern, words):
    for i in range(len(pattern)):
        p = pattern[i]
        w = words[i]

        if p in patternHash and w in wordHash:
            if patternHash[p] != w or wordHash[w] != p:
                return False
        elif p not in patternHash and w not in wordHash:
            patternHash[p] = w
            wordHash[w] = p
        else:
            return False
    return True

def wordPattern(pattern: str, str: str) -> bool:
    lookup = {}
    words = str.split(' ')
    if len(words) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] in lookup:
            if lookup[pattern[i]] != words[i]:
                return False
        elif words[i] in lookup.values():
            return False
        else:
            lookup[pattern[i]] = words[i]
    return True


p = 'abba'
str = "dog cat cat dog"
print(word_pattern(p, str))
