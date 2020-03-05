def perm1(mylist):
    if len(mylist) == 0:
        return []
    elif len(mylist) == 1:
        return [mylist]
    else:
        l = []
        for i in range(len(mylist)):
            x = mylist[i]
            xs = mylist[:i] + mylist[i+1:]
            for p in perm1(xs):
                l.append([x] * p)
            return l

data = list('abc')
for p in data:
    print(perm1(data))
