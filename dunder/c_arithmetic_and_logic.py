#! /usr/bin/python3

from re import A


class ArithmeticDunderMethods:
  """ Arithmetic """

  def __add__(self, other):
    print("called when + is used")
    return True

  def __sub__(self, other):
    print("called when - is used")
    return True

  def __mul__(self, other):
    print("called when * is used")
    return True

  def __truediv__(self, other):
    print("called when / is used")
    return True

  def __floordiv__(self, other):
    print("called when // is used")
    return True

  def __mod__(self, other):
    print("called when % is used")
    return True

  def __divmod__(self, other):
    print("called when divmod is used")
    return True

  def __pow__(self, other):
    print("called when ** is used")
    return True

  def __and__(self, other):
    print("called when & is used")
    return True

  def __or__(self, other):
    print("called when | is used")
    return True

  def __xor__(self, other):
    print("called when ^ is used")
    return True

  """ Self Assigning Arithmetic """

  def __iadd__(self, other):
    print("called when += is used")
    return self

  def __isub__(self, other):
    print("called when -= is used")
    return self

  def __imul__(self, other):
    print("called when *= is used")
    return self

  def __itruediv__(self, other):
    print("called when /= is used")
    return self

  def __ifloordiv__(self, other):
    print("called when //= is used")
    return self

  def __imod__(self, other):
    print("called when %= is used")
    return self

  def __ipow__(self, other):
    print("called when **= is used")
    return self

  def __iand__(self, other):
    print("called when &= is used")
    return self

  def __ior__(self, other):
    print("called when |= is used")
    return self

  def __ixor__(self, other):
    print("called when ^= is used")
    return self


if __name__ == "__main__":
  arithmetic = ArithmeticDunderMethods()
  arithmetic + 1
  arithmetic.__add__(1)
  arithmetic - 1
  arithmetic * 1
  arithmetic / 1
  arithmetic // 1
  arithmetic % 1
  arithmetic ** 1
  arithmetic & 1
  arithmetic | 1
  arithmetic ^ 1
  print("\n")

  arithmetic += 1
  arithmetic = arithmetic.__iadd__(1)
  arithmetic -= 1
  arithmetic *= 1
  arithmetic /= 1
  arithmetic //= 1
  arithmetic %= 1
  arithmetic **= 1
  arithmetic &= 1
  arithmetic |= 1
  arithmetic ^= 1
