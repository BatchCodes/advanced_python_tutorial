#! /usr/bin/python3

class PropertiesMethods:
  def __str__(self):
    print("\ncalled when str is used")
    return "str"

  def __repr__(self):
    print("\ncalled when repr is used")
    return "repr"

  def __int__(self):
    print("\ncalled when int is used")
    return 1

  def __float__(self):
    print("\ncalled when float is used")
    return 1.0

  def __len__(self):
    print("\ncalled when len is used")
    return True

  def __hash__(self):
    print("\ncalled when hash is used")
    return True

  def __bool__(self):
    print("\ncalled when bool is used")
    return True

  def __abs__(self):
    print("\ncalled when abs is used")
    return True

  def __contains__(self, other):
    print("\ncalled when 'in' is used")
    return True


if __name__ == "__main__":
  dunder = PropertiesMethods()
  print(str(dunder))
  print(repr(dunder))
  print(int(dunder))
  print(float(dunder))
  print(len(dunder))
  print(hash(dunder))
  print(bool(dunder))
  print(abs(dunder))
  print("a" in dunder)
