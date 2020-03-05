def intersection(n1, n2):
   freq = {}
   res = []
   for x in n1:
       freq[x] = freq.get(x, 0) + 1
   for i in n2:
        if i in freq and freq[i] > 0:
            res.append(i)
            freq[i] -= 1
   return res


def intersection_for_sorted(n1, n2):
    res = []
    i, j = 0, 0
    while i < len(n1) and j < len(n2):
        if n1[i] == n2[j]:
            res.append(n1[i])
            i += 1
            j += 1
        elif n1[i] > n2[j]:
            j = j + 1
        else:
            i = i + 1
    return res


n1 = [4, 9, 5]
n2 = [9, 4, 9, 8, 4]
num1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
num2 = [3, 4, 5, 6, 6]
print(intersection(n1, n2))
print(intersection_for_sorted(num1, num2))