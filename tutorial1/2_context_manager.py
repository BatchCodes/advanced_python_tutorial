#! /usr/bin/python3


class NewException(BaseException):
  pass


BaseException


def withTryFinally(func):
  print("do something")
  try:
    func()
  finally:
    print("clean-up")


class Context:
  def __enter__(self):
    print("Entering")
    return None

  def __exit__(self, errorType, value, traceback):
    if errorType == NewException:
      print("Handling Error")
      return True
    else:
      print("Exiting")


class FileContext:
  def __init__(self, name, method):
    self.file = open(name, method)

  def __enter__(self):
    print("Entering")
    return self.file

  def __exit__(self, errorType, value, traceback):
    print("Exiting")
    self.file.close()


def speak1():
  print("hell0")


def speak2():
  print("hola")


PART = 2

if __name__ == "__main__":
  if PART == 1:
    # try:
    #   speak1()
    # except:
    #   pass

    # try:
    #   speak2()
    # except:
    #   pass

    # withTryFinally(speak1)
    # withTryFinally(speak2)
    with Context():
      speak1()
      speak2()

  elif PART == 2:

    with Context():
      print("Hello")

      raise NewException()

  elif PART == 3:
    with Context() as thing:
      print(f"{thing=}")

  elif PART == 4:
    with FileContext("file.txt", "w") as f:
      print("Writing")
      f.write("Hello")
      raise
