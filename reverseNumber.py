'''x = input("enter the number : ")
y = x[len(x) - 1 : 0 : -1] + x[0]
print(y)
'''

def reverseNumber(num):
    rev = 0
    is_neg = False
    if num < 0:
        is_neg = True
        num = -num
    while(num > 0):
        rev = (rev * 10) + (num % 10)
        num = num // 10
    if is_neg:
        return -rev
    else:
        return rev
   # print("Reverse of this number is = %d" %rev)



num = int(input("Enter a number: "))
print(reverseNumber(num))
