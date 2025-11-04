import random
s = [12, 6, 7, 53, 2]

def push(s, e):
    s.append(e)
    return s

def pop(s):
    s.pop()
    return s

while True:
    if(random.randint(1, 999999) == 1):
        s = push(s, random.randint(1, 99))
        print(s, "push!")

    if(random.randint(1, 999999) == 1):
        s = pop(s)
        print(s, "pop!")

    if((len(s) > 8) or (len(s) < 3)):
        print("Loop exited because list got too long or short")
        break