# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# Comments are first attempt

import math

class Line():

  def __init__(self,coor1,coor2):
    # self.coor1_x = coor1[0]
    # self.coor1_y = coor1[1]
    # self.coor2_x = coor2[0]
    # self.coor2_y = coor2[1]
    self.coor1 = coor1
    self.coor2 = coor2

  def distance(self):
    # return math.sqrt((self.coor2_x-self.coor1_x)**2 + (self.coor2_y-self.coor1_y)**2)
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

  def slope(self):
    # return (self.coor2_y-self.coor1_y)/(self.coor2_x-self.coor1_x)
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return (y2-y1)/(x2-x1)