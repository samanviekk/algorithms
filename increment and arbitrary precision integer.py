def plus_one_naive(n):
    res = int("".join(map(str, n)))
    res = res + 1
    x1 = [int(x) for x in str(res)]
    return x1

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        print(A[i])
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

digits = [1, 3, 9]
print(plus_one_naive(digits))
print(plus_one(digits))
