#! /usr/bin/python3

"""
Make a class that appears to be less than 4 and greater than 5
__lt__ and __gt__
assert ci < 4 and ci > 5
assert (
  ci < 4 
  and not ci < 5
  and ci > 5
  and not ci > 4
)

Make a Loud Dictionary, i.e. a dictionary that prints out values that are set and retrieved
__setitem__ and __getitem__

Make a Loud Class Instance, i.e. a class that prints out values that are set and retrieved
__setattr__ and __getattribute__

"""


class FuckedUpNumber:
  def __lt__(self, other):
    if other == 4:
      return True
    if other == 5:
      return False

  def __gt__(self, other):
    if other == 4:
      return False
    if other == 5:
      return True


class LoudDict:
  def __init__(self):
    self.dict = dict()

  def __setitem__(self, key, value):
    print(f"setting {key} to {value}")
    self.dict[key] = value
    return True

  def __getitem__(self, key):
    print(f"getting {key}")
    return self.dict[key]


class LoudDictTwo(dict):
  def __setitem__(self, key, value):
    print(f"setting {key} to {value}")
    super().__setitem__(key, value)
    return True

  def __getitem__(self, key):
    print(f"getting {key}")
    return super().__getitem__(key)


if __name__ == "__main__":
  fun = FuckedUpNumber()

  assert (
      fun < 4
      and fun > 5
      and not fun < 5
      and not fun > 4
  )

  ld = LoudDictTwo()
  ld["one"] = 1
  ld["two"] = 2
  ld["one"]

  li = LoudInt(1)
  li += 5
  print(li)
