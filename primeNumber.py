/def generatePrime(k):
    primelist = []
    primelist.append(2)
    res = 0
    for num in range(3, k + 1):
        match = False
        for i in range(0, len(primelist)):
            if num % primelist[i] == 0:
                match = True
                break

        if not match:
            primelist.append(num)

    return primelist


print(generatePrime(50))
'''

def genPrime(n):
    for val in range(2, n + 1):
        if val > 1:
            for n in range(2, val):
                if val % n == 0:
                    break
            else:
                print(val, end = ',')

'''
