import math
def area_circle(r):
    return math.pi * r * r
circumference = lambda r: 2 * math.pi * r
try:
    radius = float(input("enter radius: "))
    area = area_circle(radius)
    circ = circumference(radius)
    print("area: {:.2f}".format(area))
    print("circumference: {:.2f}".format(circ))
except ValueError:
    print("please enter a valid numeric radius")

input("_________________________")