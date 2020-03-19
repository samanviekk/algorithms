def topKFrequent(words, k):
    lookup = {}
    for i in words:
        lookup[i] = lookup.get(i, 0) + 1
    print(lookup)


inputlist = ["day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
res = topKFrequent(inputlist, 2)
print(res)