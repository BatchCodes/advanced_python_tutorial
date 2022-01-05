#! /usr/bin/python3

class Dunder():
  def __init__(self):
    self.thing = None

  def __repr__(self) -> str:
    return f"The reprisentation of Dunder is {self.thing}"

  def __new__(cls, *args, **kwargs):
    print("Dunder was instantiated")
    return super(Dunder, cls).__new__(cls, *args, **kwargs)

  def __bool__(self):
    return True

  def __setattr__(self, name, value):
    print(f"{name} was set to {value}")
    self.__dict__[name] = value

  def __getattribute__(self, name):
    print(f"{name} was gotten")

    return object.__getattribute__(self, name)

  def __getattr(self, name):
    self.__dict__[name] = 0
    return 0


PART = 1

if __name__ == '__main__':

  if PART == 1:
    a = Dunder()
    print(a)

  elif PART == 2:
    a = Dunder()

    a.thing = 10
    a.thang = 20
    print(a.thang)

    print()
