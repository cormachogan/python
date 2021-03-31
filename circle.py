#!/usr/bin/python3
#
# We can use `circle.pi` to get pi. We can also `self.pi`, `self.__class__.pi`, or `type(self).pi`
# `self.pi` accesses the instance's private copy; we should use that if we plan to have `pi` change in different instances. 
# We can use `circle.pi` if we plan for `pi` to stay the same, or maybe change for every instance.
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
    return circle.pi * self.radius **2
  def perimeter(self):
    "calculate the perimeter of the circle"
    return self.diameter() * circle.pi
#
# Set the radius to 7
#
c = circle(7)

#
# Print info about the circle
#
print('Area', c.area())
print('Diameter', c.diameter())
print('Perimeter', c.perimeter())
