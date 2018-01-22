import math
class point():
    x=0
    y=0

p1=point()

p2=point()
p2.x =1
p2.y =1

def distance_between_points(p1,p2):
    distance=math.sqrt((p1.x-p2.x)**2+(p2.y-p1.y)**2)
    return distance

print(distance_between_points(p1,p2))

