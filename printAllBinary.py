def printAllBinary(n):
    printAllBinaryHelper(n, "")


def printAllBinaryHelper(n, output):
    if n == 0:
        print(output)
        return
    printAllBinaryHelper(n - 1, output + '0')
    printAllBinaryHelper(n - 1, output + '1')


printAllBinary(2)
