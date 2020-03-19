def roll_dice(n, sum):
    res = []
    choice = []
    roll_dice_helper(n, sum, choice, res)
    return res


def roll_dice_helper(n, sum, choice, res):

    if n == 0:
        if sum == 0:
            mylist = tuple(choice)
            res.append(mylist)
            #res.append(choice[:])
        return
    for i in range(1, 7):
        choice.append(i)
        roll_dice_helper(n - 1, sum - i, choice , res)
        choice.pop()


res = roll_dice(3, 6)
print(res)