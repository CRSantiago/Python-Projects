from Line import Line
from Cylinder import Cylinder

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print('Line Equation Test')
print(li.distance())
print(li.slope())

c = Cylinder(2,3)

print('Cylinder Equation Test')
print(c.volume())
print(c.surface_area())