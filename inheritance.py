#!/usr/bin/python3

# Inheritance means that you can create a new object and avoid re-defining some parts of it.
# Instead you can use parts of another object.
#

# This is useful if you have different levels of abstractions, and want to avoid re-defining
# the parts that are in common.

# When a class is created, it is possible to specify its inheritance by specifying the name of
# the "parent" class in parenthesis in the definition of the class

# super() is a way to get access to the "parent" of the class, or in other words, the object
# from which this object inherits. You can use the unmodified methods and properties, such
# as __noise__ from the dog object as in the case of the terrier class below.
#

class animal:
  def eat(self, food):
    print('the', type(self).__name__, 'eats', food)

class cat(animal):
  def noise(self):
    print('the', type(self).__name__, 'says meow')

class dog(animal):
  def noise(self):
    print('the', type(self).__name__, 'says woof')

class terrier(dog):
  def noise(self):
    for _ in range(10):
      super().noise()

a = animal()
a.eat('cake')

b = cat()
b.noise()
b.eat('fish')

c = dog()
c.noise()
c.eat('meat')

d = terrier()
d.noise()
d.eat('kibble')


isinstance(d, dog)
isinstance(d, animal)
isinstance(d, cat)
