#! /usr/bin/python3
from random import randint


class DemoClass:
  def __init__(self, thing, thang, theng):
    # self.count = 0
    self.__dict__["count"] = 0
    self.thing = thing
    self.thang = thang
    self.theng = theng

  def __len__(self):
    return randint(5, 20)

  def __setattr__(self, __name: str, __value: object):

    self.__dict__["count"] += 1
    self.__dict__[__name] = __value

  def __add__(self, other):
    print("Look Mukku, no hands")

    return True


class InternalWorkingsMethods:
  thing = 5

  def __init__(self):
    print("\ncalled when object is created")

  def __getattribute__(self, __name: str):
    print("\ncalled when object.__name__ is used")
    return True

  def __setattr__(self, __name: str, __value: object):
    print("\ncalled when object.__name__ = __value is used")
    return True

  def __delattr__(self, __name: str):
    print("\ncalled when del object.__name__ is used")
    return True


if __name__ == "__main__":
  # dunder = InternalWorkingsMethods()
  # print(dunder.thing)
  # dunder.thing = 6
  # del dunder.thing

  dc = DemoClass(1, 2, 3)
  print(len(dc))
  print(len(dc))
  print(len(dc))
  print(len(dc))
  print(len(dc))
  print(f"{dc.count=}")
