def print_subset(s):
    res = []
    print_subset_helper(s, 0, "", res)
    return res

def print_subset_helper(s, index, myset, res):
    if index == len(s):
        res.append(myset)
        return
    # exclude
    print_subset_helper(s, index + 1, myset, res)
    # include
    myset = myset + s[index]
    print_subset_helper(s, index + 1, myset, res)


res = print_subset('abcd')
print(res)