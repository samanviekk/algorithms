from queue import LifoQueue

mystack = LifoQueue()

def wellformed(mylist):

    for i in range(0, len(mylist) - 1):
        if mylist[i] == '(':
            mystack.get(mylist[i])

        if mylist[i] == ')':
            if mystack.put()
