def printAllDecimal(n):
    printAllDecimalHelper(n, "")


def printAllDecimalHelper(n, output):
    if n == 0:
        print(output)
        return
    for i in range(10):
        printAllDecimalHelper(n - 1, output + str(i))


printAllDecimal(2)
