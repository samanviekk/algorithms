def groupAnagrams(strs):

    lookup = {}
    for i in strs:
        key = ''.join(sorted(i))
        if key not in lookup:
            lookup[key] = [i]
        else:
            lookup[key].append(i)
    return list(lookup.values())





strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
print(res)
