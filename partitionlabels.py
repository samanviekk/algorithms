def partitionLabels(S):
    res = []
    lookup = {}
    #lookup = {c: i for i, c in enumerate(S)}
    #for i in range(0, len(S)):
     #   lookup[S[i]] = i
    for i, c in enumerate(S):
        lookup[c] = i
    print(lookup.items())

    start = 0
    end = 0
    #for i in range(0, len(S)):
    for i, c in enumerate(S):
        end = max(end, lookup[c])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res

S = "ababcbacadefegdehijhklij"
res = partitionLabels(S)
print(res)