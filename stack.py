import random, time

s = [12, 6, 7, 53, 2]



def push(s, e):
    s.append(e)
    return s

def pop(s):
    s.pop()
    return s

active = True
epoch = time.time()
while active:
    timer = time.time() - epoch
    if(random.randint(1, 999999) == 1):#if(timer % 2 == 0):
        s = push(s, random.randint(1, 99))
        print(s, "push!")

    if(random.randint(1, 999999) == 1):#if(timer % 3 == 0):
        s = pop(s)
        print(s, "pop!")

    if((len(s) > 8) or (len(s) < 3)):
        print("Loop exited because list got too long or short")
        active = False