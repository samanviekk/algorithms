def add_string(A, B):
    carry = 0
    i = len(A) - 1
    j = len(B) - 1
    res = []
    while i >= 0 or j >= 0:
        if i < 0: a = 0
        else:
            a = A[i]
            i -= 1
        if j < 0: b = 0
        else:
            b = B[j]
            j -= 1
        x = int(a) + int(b) + carry
        if x > 10:
            carry = 1
            x = x - 10
        res. append(str(x))
    if carry:
        res. append(str(carry))
    res.reverse()
    return res


A = ['2', '8', '7']
B = ['4', '5']
res = add_string(A, B)
print(res)