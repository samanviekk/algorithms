'''def removeDuplicates(A, key):
    k = 0
    for i in range(0, len(A)):
        if A[i] != key:
            A[k] = A[i]
            k = k + 1

'''

def rem_dup(A):
    k = 2
    for i in range(2, len(A)):
        if A[k-2] != A[i]:
            A[k] = A[i]
            k = k + 1
    del A[k:]

A = [1, 1, 1, 1, 5]
rem_dup(A)
A = [str(i) for i in A]
A = " ".join(A)
A += " "
print(A)