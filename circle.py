#
# -- To run:
#
# c = circle(7)
# print('Area', c.area())
# print('Diameter', c.diameter())
# print('Perimeter', c.perimeter())
#
class circle:
  """
  A circle object is created from a radius, default is 1
  """
  pi = 3.141529
  def __init__(self, radius=1):
    "Initialise the circle from the specified radius"
    self.radius = radius
  def diameter(self):
    "Return twice the radius"
    return self.radius * 2
  def area(self):
    "calculate the area of the circle"
#
# We are using `circle.pi` to get pi. We could also have used `self.pi`, `self.__class__`, or `type(self).pi`
#
    return circle.pi * self.radius **2
  def perimeter(self):
    "calculate the perimeter of the circle"
    return self.diameter() * circle.pi
    
