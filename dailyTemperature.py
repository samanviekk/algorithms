def dailyTemperatures(A):
    res = []
    for i in range(len(A)):
        found = False
        for j in range(i + 1, len(A)):
            if A[i] < A[j]:
                res.append(j - i)
                found = True
                break
        if found == False:
            res.append(0)
    return res

def dailyTemp(A): # using stack
    mystack = []
    res = [0] * len(A)
    for i in range(len(A)):
        while len(mystack) > 0 and A[i] > A[mystack[-1]]:
            res[mystack[-1]] = (i - mystack[-1])
            mystack.pop()
        mystack.append(i)
    return res


A = [73, 74, 75, 71, 69, 72, 76, 73]
res = dailyTemperatures(A)
print(res)
res1 = dailyTemp(A)
print(res1)
