import os

def fibbonachi(num):
    temp = [0, 1]
    if num < 3:
        return temp
    for i in range(2, num):
        temp.append(temp[i-1] + temp[i-2])
    return temp

os.system('clear')


for i in range(2, 15):
    print(fibbonachi(i))