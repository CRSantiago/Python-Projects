class Cylinder():

  pie = 3.14

  def __init__(self, height=1,radius=1):
    self.height = height
    self.radius = radius

  def volume(self):
    return (Cylinder.pie) * (self.radius**2) * (self.height)

  def surface_area(self):
    return (2 * Cylinder.pie * self.radius * self.height) + (2 * Cylinder.pie * (self.radius**2))