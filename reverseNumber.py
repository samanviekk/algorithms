'''x = input("enter the number : ")
y = x[len(x) - 1 : 0 : -1] + x[0]
print(y)
'''

def reverseNumber(num):
    rev = 0
    while(num > 0):
        rev = (rev * 10) + (num % 10)
        num = num // 10
    print("Reverse of this number is = %d" %rev)

num = int(input("Enter a number: "))
reverseNumber(num)
