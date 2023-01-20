#! /usr/bin/python3

""" Method Decorators """


def decrementCount(func):
  def funcWrapper(self, *args, **kwargs):
    self.count -= 1
    print(f"\n{self.count = }")
    func(self, *args, **kwargs)

  return funcWrapper


def actuallyJustSaysHi(func):
  def funcWrapper(self, *args, **kwargs):
    print("Hi")
  return funcWrapper


class Decorators:
  def __init__(self):
    self._thing = None
    self.count = 0

  @staticmethod
  def speak():
    print("Hello There")

  @property
  def thing(self):
    print("Providing thing")
    return self._thing

  @thing.setter
  def thing(self, value):
    print("Setting thing")
    newThing = str(value)

    self._thing = newThing

  def incrementCount(func):
    def funcWrapper(self, *args, **kwargs):
      self.count += 1
      print(f"\n{self.count = }")
      func(self, *args, **kwargs)

    return funcWrapper

  # @decrementCount
  @actuallyJustSaysHi
  def add2(self, value):
    with2Added = value+2
    print(f"{with2Added = }")
    return with2Added


if __name__ == "__main__":
  d = Decorators()
  # d.speak()
  d.add2(1)
  d.add2(2)
  d.add2(3)

  # print(d.thing)

  # d.thing = 5
  # print(type(d.thing))

  d.add2(1)
  d.add2(2)
  d.add2(3)
