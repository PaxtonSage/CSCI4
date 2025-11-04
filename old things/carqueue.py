import random
import time

class Car:
    def __init__(self, id, gasTankfull):
        self.id = id
        self.gasTankFull = gasTankfull


cars = []
carsNum = 10
for i in range(0, carsNum):
    cars.append(Car(i, False))
    #print(cars[i])

queue = []
stationReady = False
carTimer = time.time()
gasTimer = time.time()

def printInfo():
    print("Queue: ", queue)
    print("Car ID at front", queue[len(queue)-1].id)

def pushCar():
    pass

while True:
    if (time.time() - carTimer) > 2:
        carTimer = time.time()
        holder = cars[random.randint(0, carsNum-1)]
        if ((holder in queue) or holder.gasTankFull): continue
        queue.insert(0, holder)

        printInfo()
    if(len(queue) > 0):
        if (queue[len(queue)-1] and (time.time() - gasTimer) > 4):
            gasTimer = time.time()
            queue[len(queue)-1].gasTankFull = True
            queue.pop()
            stationReady = True
