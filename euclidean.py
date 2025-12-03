point1 = [-6, 6] #define first point [x, y]
point2 = [6, -6] #define second point [x, y]

def distance(p1, p2): #define function 'distance' which takes in two points, p1 and p2
    dx = p1[0] - p2[0] #set the variable 'dx' equal to the horizontal distance between p1 and p2
    dy = p1[1] - p2[1] #set the variable 'dy' equal to the vertical distance between the points
    dist = pow((dx*dx) + (dy*dy), .5) #set the variable 'dist' equal to the distance between the two points using the pythagorean theorum with the horizontal and vertical distances being the inputs 
    return dist #returns the distance between the points

print(distance(point1, point2)) #prints out the distance between point1 and point2 using the distance function defined above