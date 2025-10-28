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
    print(cars[i])

queue = []
stationReady = False
timer = time.time()
while True:

    if (time.time() - timer) > 3:
            
            queue.insert(0)



    if stationReady:
        cars[cars.count].gasTankFull = True
        cars.remove[cars.count]
