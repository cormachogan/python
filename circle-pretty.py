#!/usr/bin/python3

# Demo the use of `repr` and `str`
# If `__str__` is not present, python falls back to using `__repr__`
# This script can be run with and without `__str__` defined to compare the differences
# print uses `__str__` but python will fall back to using `__repr__` if it is not defined (useful for troubleshooting)
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
  def __repr__(self):
    "representation of a circle"
    return '{0}({1})'.format(self.__class__.__name__, self.radius)
  def __str__(self):
    "Pretty representation of a circle"
    return 'circle with radius: {r:.6f}, diameter(d:.6f) area: {a:.6f}, perimeter: {p:.6f}'.format(r=self.radius, d=self.diameter(), a=self.area(), p=self.perimeter())

c = circle()
print(c)
print(repr(c))
print(str(c))
