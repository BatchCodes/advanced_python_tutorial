#! /usr/bin/python3

class DemoClass:
  def __init__(self, thing, thang, theng):
    self.thing = thing
    self.thang = thang
    self.theng = theng

  def __str__(self):
    return f"{self.thing=}, {self.thang=}, {self.theng=}"


class ActionDunderMethods:
  def __call__(self, *args, **kwargs):
    print("\ncalled when object() is used")
    return True

  def __getitem__(self, key):
    print("\ncalled when object[key] is used")
    return True

  def __setitem__(self, key, value):
    print("\ncalled when object[key] = value is used")
    return True

  def __delitem__(self, key):
    print("\ncalled when del object[key] is used")
    return True


if __name__ == "__main__":
  dc = DemoClass(1, 2, 3)
  print(dc.__dict__)
  # dunder = ActionDunderMethods()
  # dunder(1, 2, 3)
  # dunder[1]
  # dunder[1] = 2
  # del dunder[1]
