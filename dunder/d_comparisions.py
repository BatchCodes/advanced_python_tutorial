#! /usr/bin/python3

class ComparisonDunderMethods:
  def __eq__(self, other):
    print("\ncalled when == is used")
    return True

  def __ne__(self, other):
    print("\ncalled when != is used")
    return True

  def __lt__(self, other):
    print("\ncalled when < is used")
    return True

  def __le__(self, other):
    print("\ncalled when <= is used")
    return True

  def __gt__(self, other):
    print("\ncalled when > is used")
    return True

  def __ge__(self, other):
    print("\ncalled when >= is used")
    return True


if __name__ == "__main__":
  dunder = ComparisonDunderMethods()
  dunder == 1
  dunder != 1
  dunder < 1
  dunder <= 1
  dunder > 1
  dunder >= 1
