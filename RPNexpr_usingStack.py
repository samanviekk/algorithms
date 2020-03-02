def evaluate(expr):
    results = []
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for i in expr.split(','):
        if i in OPERATORS:
            results.append(OPERATORS[i](results.pop(), results.pop()))
        else: # if i is a number
            results.append(int(i))
    return results[-1]


expression = "3,4,+,2,*,1,+"
print(evaluate(expression))


