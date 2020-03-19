def count_climbing_stairs(n, steps, count):
    if n == 0:
        count[0] += 1
        return
    if n < 0:
        return
    for i in steps:
        count_climbing_stairs(n - i, steps, count)



steps = [1, 2]
count = [0]
count_climbing_stairs(5, steps, count)
print(count)